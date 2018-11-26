"""
Module containing a sentiment analysis plugin.  Based on the TextBlob library
(itself based upon the indomitable NLTK Libraries), which provides sentiment
analysis out of the box.  This plugin will attempt to create sentiment scores
when passed tweet information.
"""
import logging

import textblob.download_corpora as td

from textblob import TextBlob

from ingress.data_processing.processing import PluginBase

LOG = logging.getLogger(__name__)


class SentimentAnalysis(PluginBase):
    """
    Class implementing a sentiment analysis plugin.  Wraps the TextBlob library.
    """

    def __init__(self, *args, **kwargs):

        # Ensure we have the various corpora that we need for analysis works.
        td.download_all()

        super().__init__(*args, **kwargs)

    def process_tweet(self, tweet_json):
        """
        Attempt to analyse sentiment of the given tweet data.
        """
        # pull either the tweet text, or the tweet full text depending on
        # whether the tweet was truncated
        sentence_data = ''
        if tweet_json.get('truncated'):
            sentence_data = tweet_json.get('extended_tweet').get('full_text')

        else:
            sentence_data = tweet_json.get('text')

        LOG.debug('Analysing the following sentence for sentiment: %s', sentence_data)
        if not sentence_data:
            return tweet_json

        blob = TextBlob(sentence_data)

        tweet_json['sentiment_polarity'] = blob.sentiment.polarity
        tweet_json['sentiment_subjectivity'] = blob.sentiment.subjectivity
        tweet_json['tweet_length'] = len(blob.words)
        LOG.info(
            'Polarity: %s, Subjectivity: %s Word Count: %s',
            tweet_json['sentiment_polarity'],
            tweet_json['sentiment_subjectivity'],
            tweet_json['tweet_length']
        )

        return tweet_json
