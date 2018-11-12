"""
Module contains Tweepy listener classes, which are used to process tweets that
the Tweepy Stream instance receives from twitter.
"""
import json
import logging

import tweepy

from ingress.geocode import get_geotagger

LOG = logging.getLogger(__name__)


class StdOutListener(tweepy.StreamListener):
    """
    Simple class that provides a stream processor that logs tweet text to the console.
    """
    total_tweets = []

    def __init__(self, *args, **kwargs):
        self.geotagger = get_geotagger()
        self.tweets = []

        super().__init__(*args, **kwargs)

    def on_data(self, raw_data):
        """
        Event handler called whenever new data is pushed to the Tweepy Stream client.

        :param raw_data: New data is passed in as a JSON document, containing a
        variety of data and metadata about the new tweet.
        """
        tweet = json.loads(raw_data)
        LOG.debug('Received a tweet: %s', tweet['text'])
        tweet_location = self.geotagger.resolve_tweet(tweet)

        if tweet_location:
            LOG.debug(
                '\n########################\n'
                'Identified Tweet location: %s'
                '\n########################',
                tweet_location
            )
            tweet['location'] = repr(tweet_location)

        self.tweets.append(tweet)

        StdOutListener.total_tweets.append(tweet)
        if len(self.total_tweets) % 10 == 0:
            with open('sample.json', 'w') as output_fd:
                json.dump(self.tweets, output_fd)

            self._tweet_location_stats()

        return True

    def _tweet_location_stats(self):
        """
        Print out the percentage of tweets with location information available.
        """
        location_aware_tweets = 0
        total_tweets = len(self.tweets)

        for tweet in self.tweets:
            if 'location' in tweet:
                location_aware_tweets += 1

        LOG.info(
            '%s Total tweets of which %s included a location. (%s)',
            total_tweets,
            location_aware_tweets,
            (location_aware_tweets / total_tweets) * 100
        )

    def on_exception(self, exception=None):

        print(exception)
