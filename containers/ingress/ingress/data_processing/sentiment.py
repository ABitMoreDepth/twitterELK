"""
Module containing a sentiment analysis plugin.

Based on the TextBlob library (itself based upon the indomitable NLTK
Libraries), which provides sentiment analysis out of the box.  This plugin will
attempt to create sentiment scores when passed tweet information.
"""

import logging
from typing import Any, cast, Dict, Union

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
    """Simple Elasticsearch DSL mapping of the text data this plugin will return."""

    full_text = es.Text()
    pattern_polarity = es.Float()
    pattern_subjectivity = es.Float()
    short_text = es.Text()
    translated = es.Text()
    truncated = es.Boolean()
    tweet_length = es.Integer()
    vader_compound = es.Float()
    vader_compound_inverted = es.Float()
    vader_negative = es.Float()
    vader_neutral = es.Float()
    vader_positive = es.Float()


class SentimentAnalysis(PluginBase):
    """Class implementing a sentiment analysis plugin.  Wraps the TextBlob library."""

    data_schema = {"text": es.Object(Text)}

    def __init__(self, *args, **kwargs) -> None:
        """Initialise SentimentAnalysis instance, ensure we have downloaded required data."""
        # Ensure we have the various corpora that we need for analysis works.
        text_blob_download()
        nltk_download('vader_lexicon')

        # Initialise the Vader sentiment analysis tool
        self.analyser = SentimentIntensityAnalyzer()

        super().__init__(*args, **kwargs)  # type: ignore

    def process_tweet(self, tweet_json: Dict[str, Any]) -> Dict[str, Any]:
        """Attempt to analyse sentiment of the given tweet data."""
        # pull either the tweet text, or the tweet full text depending on
        # whether the tweet was truncated
        if not tweet_json:
            return tweet_json

        raw_tweet: Dict[str, Any] = cast(Dict[str, Any], tweet_json.get('_raw'))
        if not raw_tweet:
            return tweet_json

        text_processing: Dict[str, Any] = {}
        text_processing['short_text'] = raw_tweet['text']
        text_processing['truncated'] = raw_tweet['truncated']
        if text_processing['truncated']:
            text_processing['full_text'] = raw_tweet['extended_tweet']['full_text']

        tweet_text = (
            text_processing['full_text']
            if text_processing['truncated'] else text_processing['short_text']
        )

        text_processing.update(
            self._blob_process_tweet(
                tweet_text=tweet_text,
                tweet_lang=raw_tweet['lang'],
            )
        )

        # NLTK Vader sentiment analysis - translated field is created during
        # the text blob processing.
        text_processing.update(self._vader_classify(text_processing['translated']))

        LOG.info(
            'Polarity: %s, Subjectivity: %s, Word Count: %s, Language: %s',
            text_processing['pattern_polarity'],
            text_processing['pattern_subjectivity'],
            text_processing['tweet_length'],
            raw_tweet['lang']
        )

        tweet_json['text'] = text_processing

        return tweet_json

    @staticmethod
    def _blob_process_tweet(tweet_text: str, tweet_lang: str) -> Dict[str, Any]:
        """Analyse tweet text using the TextBlob class."""
        text_processing: Dict[str, Union[str, int]] = {}

        blob = TextBlob(tweet_text)
        if not blob:
            return {}

        try:
            if tweet_lang not in ('en', 'und', None):
                LOG.debug('Attempting to translate from %s to English', tweet_lang)
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

        text_processing['tweet_length'] = len(blob.words)

        return text_processing

    def _vader_classify(self, tweet_text: str) -> Dict[str, Any]:
        """Analyse tweet text for sentiment using NLTK Vader Algorithm."""
        # NLTK Vader sentiment analysis.
        text_processing: Dict[str, float] = {}
        sentiment_scores = self.analyser.polarity_scores(tweet_text)
        if any(sentiment_scores):
            # Make sure we have something to dump into the output data.
            # {'neg': 0.347, 'neu': 0.653, 'pos': 0.0, 'compound': -0.1511}
            text_processing['vader_negative'] = sentiment_scores['neg']
            text_processing['vader_neutral'] = sentiment_scores['neu']
            text_processing['vader_positive'] = sentiment_scores['pos']
            text_processing['vader_compound'] = sentiment_scores['compound']
            text_processing['vader_compound_inverted'] = sentiment_scores['compound'] * -1

        return text_processing
