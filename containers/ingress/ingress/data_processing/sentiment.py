"""
Module containing a sentiment analysis plugin.  Based on the TextBlob library
(itself based upon the indomitable NLTK Libraries), which provides sentiment
analysis out of the box.  This plugin will attempt to create sentiment scores
when passed tweet information.
"""
import logging

from nltk import download as nltk_download
from nltk.sentiment import SentimentIntensityAnalyzer
from tenacity import retry, stop_after_attempt, wait_fixed, RetryError
from textblob import TextBlob
from textblob.download_corpora import download_all as text_blob_download
from textblob.exceptions import NotTranslated

import elasticsearch_dsl as es

from ingress.structures import PluginBase

LOG = logging.getLogger(__name__)


class Text(es.InnerDoc):
    """
    Simple Elasticsearch DSL mapping of the text data this plugin will return.
    """
    full_text = es.Text()
    short_text = es.Text()
    truncated = es.Boolean()
    pattern_polarity = es.Float()
    pattern_subjectivity = es.Float()
    translated = es.Text()
    tweet_length = es.Integer()
    vader_compound = es.Float()
    vader_negative = es.Float()
    vader_neutral = es.Float()
    vader_positive = es.Float()


class SentimentAnalysis(PluginBase):
    """
    Class implementing a sentiment analysis plugin.  Wraps the TextBlob library.
    """
    data_schema = {"text": es.Object(Text)}

    def __init__(self, *args, **kwargs):

        # Ensure we have the various corpora that we need for analysis works.
        text_blob_download()
        nltk_download('vader_lexicon')

        # Initialise the Vader sentiment analysis tool
        self.analyser = SentimentIntensityAnalyzer()

        super().__init__(*args, **kwargs)

    def process_tweet(self, tweet_json=None):
        """
        Attempt to analyse sentiment of the given tweet data.
        """
        # pull either the tweet text, or the tweet full text depending on
        # whether the tweet was truncated
        if not tweet_json:
            return tweet_json

        text_processing = {}
        text_processing['short_text'] = tweet_json['_raw']['text']
        text_processing['truncated'] = tweet_json['_raw']['truncated']
        if text_processing['truncated']:
            text_processing['full_text'] = tweet_json['_raw']['extended_tweet']['full_text']

        blob = TextBlob(
            text_processing['full_text']
            if text_processing['truncated'] else text_processing['short_text']
        )
        if not blob:
            return tweet_json

        try:
            blob_language = tweet_json.get('_raw').get('lang')
            if blob_language not in ('en', 'und'):
                LOG.debug('Attempting to translate from %s to English', blob_language)
                # We make use of the Tenacity retry library here to simplify
                # repeating a function call, however the default implementation
                # is a decorator, hence the pair of calls here, which return a
                # wrapped function which will deal with retries.
                retrying_translator = retry(
                    stop=stop_after_attempt(5),
                    wait=wait_fixed(0.5)
                )(
                    blob.translate
                )
                new_blob = retrying_translator(to='en')
                blob = new_blob
        except NotTranslated:
            pass
        except RetryError:
            LOG.error('Unable to translate tweet contents: %s', str(blob))

        text_processing['translated'] = str(blob)

        LOG.debug(
            'Analysing the following sentence for sentiment: %s',
            text_processing['translated']
        )

        # TextBlob based sentiment analysis, based on the Pattern Analyser,
        text_processing['pattern_polarity'] = blob.sentiment.polarity
        text_processing['pattern_subjectivity'] = blob.sentiment.subjectivity

        # NLTK Vader sentiment analysis.
        sentiment_scores = self.analyser.polarity_scores(text_processing['translated'])
        if any(sentiment_scores):
            # Make sure we have something to dump into the output data.
            # {'neg': 0.347, 'neu': 0.653, 'pos': 0.0, 'compound': -0.1511}
            text_processing['vader_negative'] = sentiment_scores['neg']
            text_processing['vader_neutral'] = sentiment_scores['neu']
            text_processing['vader_positive'] = sentiment_scores['pos']
            text_processing['vader_compound'] = sentiment_scores['compound']

        text_processing['tweet_length'] = len(blob.words)
        LOG.info(
            'Polarity: %s, Subjectivity: %s, Word Count: %s, Language: %s',
            text_processing['pattern_polarity'],
            text_processing['pattern_subjectivity'],
            text_processing['tweet_length'],
            tweet_json['_raw']['lang']
        )

        tweet_json['text'] = text_processing

        return tweet_json
