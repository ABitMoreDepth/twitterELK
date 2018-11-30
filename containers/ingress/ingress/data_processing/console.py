"""
This module contains a simple plugin which simply emits tweet data to the console.
"""

import logging
from pprint import pformat

from ingress.structures import PluginBase


LOG = logging.getLogger(__name__)


class Console(PluginBase):
    """
    Class that will emit tweet data to the console.
    """
    process_order = 10

    def process_tweet(self, tweet_json=None):
        """
        Log the tweet to the console.
        """
        LOG.debug('Received new tweet data: %s', pformat(tweet_json, indent=4))

        return tweet_json
