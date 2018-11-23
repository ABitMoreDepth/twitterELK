"""
Contains the primary entrypoint and exit handling code for the Twitter Ingress tooling.
"""

import logging
import sys

#  from concurrent.futures import ThreadPoolExecutor
from os import environ

import tweepy

#  from ingress.listeners import StdOutListener
#  from ingress.listeners import ESListener
from ingress.structures import get_api_instance, get_processor_instance
from ingress.listeners import QueueListener

#  from ingress.data_processing.processing import DataProcessor
from ingress.data_processing.processing import PluginBase

LOG = logging.getLogger(__name__)


def shutdown(exit_code=0):
    """
    Safely close down the ingress application.

    :param exit_code: raise a system exit with the provided exit code.  Defaults to 0.
    """
    pass


def main():
    """
    Primary entrypoint to the Twitter Ingress tool.  Sets up access to twitter
    based on secrets stored locally on the filesystem and connects to twitter
    to start consuming tweets.
    """

    LOG.debug('Loading twitter authentication confifg')
    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    oauth_key = environ['OAUTH_KEY']
    oauth_secret = environ['OAUTH_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(oauth_key, oauth_secret)

    LOG.debug('Creating Stream instance')
    api = get_api_instance('api', auth=auth, listener=QueueListener())

    if 'HASHTAGS' in environ:
        tweet_filters = environ['HASHTAGS'].split(',')
    else:
        tweet_filters = ['#brexit', '#remain', '#leave']
    LOG.info('Streaming tweets matching these keywords: %s', tweet_filters)

    PluginBase.import_subclasses()
    data_processor = get_processor_instance('data_processor')

    try:
        api.filter(track=tweet_filters, async=True)
        data_processor.start()

    except KeyboardInterrupt:
        LOG.info('Caught Ctrl+C, Shutting down.')
        api.disconnect()
        data_processor.stop()
        sys.exit(0)


if __name__ == '__main__':
    main()
