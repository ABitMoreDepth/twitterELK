"""
Contains the primary entrypoint and exit handling code for the Twitter Ingress tooling.
"""

import logging
import sys

from os import environ

import tweepy

#  from ingress.listeners import StdOutListener
from ingress.listeners import ESListener

LOG = logging.getLogger(__name__)


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

    #  with open(join(dirname(__file__), '../../../.env'), 'r') as env:
    #      content = env.readlines()
    #      env_vars = {
    #          key: value
    #          for key,
    #          value in [tuple(line.strip().split('=')) for line in content]
    #      }
    #  CONSUMER_KEY'
    #  CONSUMER_SECRET'
    #  OAUTH_TOKEN'
    #  OATH_SECRET'

    #  auth = tweepy.OAuthHandler(env_vars['CONSUMER_KEY'], env_vars['CONSUMER_SECRET'])
    #  auth.set_access_token(env_vars['OAUTH_TOKEN'], env_vars['OAUTH_SECRET'])
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(oauth_key, oauth_secret)

    LOG.debug('Creating Stream instance')
    #  api = tweepy.Stream(auth=auth, listener=StdOutListener())
    api = tweepy.Stream(auth=auth, listener=ESListener())

    if 'HASHTAGS' in environ:
        tweet_filters = environ['HASHTAGS'].split(',')
    else:
        tweet_filters = ['#brexit', '#remain', '#leave']
    LOG.info('Streaming tweets matching these keywords: %s', tweet_filters)

    try:
        api.filter(track=tweet_filters)
    except KeyboardInterrupt:
        LOG.info('Caught Ctrl+C, Shutting down.')
        api.disconnect()
        sys.exit(0)


if __name__ == '__main__':
    main()
