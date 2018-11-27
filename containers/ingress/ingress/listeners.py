"""
Module contains Tweepy listener classes, which are used to process tweets that
the Tweepy Stream instance receives from twitter.
"""
import json
import logging
#  import re

import tweepy

from ingress.data_queue import DATA_QUEUE


LOG = logging.getLogger(__name__)


class QueueListener(tweepy.StreamListener):
    """
    Listener which consumes tweets from tweepy and pushes them to a queue.
    """

    def on_data(self, raw_data):
        """
        This listener is very simplistic, and will simply log the raw data to
        the queue, for other systems to consume from.
        """
        try:
            json_data = json.loads(raw_data)
        except (TypeError, json.JSONDecodeError):
            LOG.error('Encountered issue attempting to parse new data.')
            return
        #  LOG.debug('Ingress received new raw_data: %s', json_data)
        LOG.debug(
            'Pushing new tweet to queue ready for processing: %s',
            json_data.get('text', None)
        )
        DATA_QUEUE.put(json_data)
