"""Contains the primary entrypoint and exit handling code for the Twitter Ingress tooling."""

import logging
import sys

from os import environ

import tweepy

from ingress.data_processing.processing import DataProcessor
from ingress.utils import get_singleton_instance, setup_mappings
from ingress.listeners import QueueListener
from ingress.structures import PluginBase, DATA_QUEUE

LOG = logging.getLogger(__name__)


def shutdown(exit_code=0) -> None:
    """
    Safely close down the ingress application.

    :param exit_code: raise a system exit with the provided exit code.  Defaults to 0.
    """
    LOG.info('Shutting Down.')
    get_singleton_instance(tweepy.Stream).disconnect()
    get_singleton_instance(DataProcessor).stop()
    sys.exit(exit_code)


def main() -> None:
    """
    Primary entrypoint to the Twitter Ingress tool.

    Sets up access to twitter based on secrets stored locally on the filesystem
    and connects to twitter to start consuming tweets.
    """
    LOG.debug('Loading twitter authentication confifg')
    consumer_key: str = environ['CONSUMER_KEY']
    consumer_secret: str = environ['CONSUMER_SECRET']
    oauth_key: str = environ['OAUTH_KEY']
    oauth_secret: str = environ['OAUTH_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(oauth_key, oauth_secret)

    LOG.debug('Creating Stream instance')
    api = get_singleton_instance(
        tweepy.Stream,
        auth=auth,
        listener=QueueListener(ignore_retweets=True)
    )

    if 'HASHTAGS' in environ:
        tweet_filters = environ['HASHTAGS'].split(',')
    else:
        tweet_filters = ['#brexit', '#remain', '#leave']
    LOG.info('Streaming tweets matching these keywords: %s', tweet_filters)

    index_suffix = '-'.join(tweet_filters).lower().replace('#', '')
    twitter_index = 'tweets-{}'.format(index_suffix)

    PluginBase.import_subclasses()
    data_processor = get_singleton_instance(
        DataProcessor,
        twitter_index=twitter_index,
        queue=DATA_QUEUE,
    )

    try:
        setup_mappings(
            index_suffix,
            environ['ES_HOST'],
        )
        api.filter(track=tweet_filters, is_async=True)
        data_processor.start()

    except KeyboardInterrupt:
        LOG.info('Caught Ctrl+C')
        shutdown()

    except Exception:  # pylint: disable = broad-except
        LOG.error('Caught Exception!', exc_info=True)
        shutdown(1)


if __name__ == '__main__':
    main()
