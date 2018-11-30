"""
Module contains Tweepy listener classes, which are used to process tweets that
the Tweepy Stream instance receives from twitter.
"""
import json
import logging
from copy import deepcopy

import arrow
import tweepy

from ingress.data_queue import DATA_QUEUE

LOG = logging.getLogger(__name__)


class QueueListener(tweepy.StreamListener):
    """
    Listener which consumes tweets from tweepy and pushes them to a queue.
    """

    def __init__(self, ignore_retweets=False, *args, **kwargs):
        self.ignore_retweets = ignore_retweets

        super().__init__(*args, **kwargs)

    def on_data(self, raw_data):
        """
        This listener is very simplistic, and will simply log the raw data to
        the queue, for other systems to consume from.
        """
        try:
            tweet = {}
            json_data = json.loads(raw_data)
            if self.ignore_retweets and 'retweeted_status' in json_data:
                LOG.info('Skipping Retweet')
                return

            tweet['_raw'] = deepcopy(json_data)
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
        DATA_QUEUE.put(tweet)
