"""
Module contains Tweepy listener classes.

These are used to process tweets that the Tweepy Stream instance receives from twitter.
"""

import json
import logging
from copy import deepcopy

import arrow
import tweepy

#  from ingress.structures import DATA_QUEUE
from ingress.celery import process_tweet

LOG = logging.getLogger(__name__)


class QueueListener(tweepy.StreamListener):
    """
    Listener which consumes tweets from tweepy and pushes them to a queue.

    This listener merely creates a base dict with all the raw data received
    from twitter serialised into python data structures, and pushes it to a
    Queue, for further processing elsewhere.
    """

    def __init__(self, twitter_index: str, ignore_retweets: bool = False, *args, **kwargs):
        """Initialise instance variables."""
        self.ignore_retweets = ignore_retweets
        self.twitter_index = twitter_index

        super().__init__(*args, **kwargs)

    def on_data(self, raw_data):
        """Called when a new tweet is passed to us, serialise and push to a queue."""
        try:
            tweet = {}
            json_data = json.loads(raw_data)
            if self.ignore_retweets and 'retweeted_status' in json_data:
                LOG.info('Skipping Retweet')
                return

            tweet['_raw'] = deepcopy(json_data)
            # Twitter for some reason gives us time since epoch in miliseconds,
            # whilst Arrow works off of time in seconds when given an integer,
            # hence the division by 1000 here.
            tweet['timestamp'] = arrow.get(int(json_data.get('timestamp_ms')) / 1000).datetime
        except (TypeError, json.JSONDecodeError):
            LOG.error('Encountered issue attempting to parse new data.')
            return
        #  LOG.debug('Ingress received new raw_data: %s', json_data)
        LOG.debug(
            'Pushing new tweet to queue ready for processing: %s',
            json_data.get('text',
                          None)
        )
        #  DATA_QUEUE.put(tweet)
        process_tweet.delay(twitter_index=self.twitter_index, tweet_data=tweet)
