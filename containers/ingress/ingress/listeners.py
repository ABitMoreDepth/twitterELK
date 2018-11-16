"""
Module contains Tweepy listener classes, which are used to process tweets that
the Tweepy Stream instance receives from twitter.
"""
import json
import logging
import re

import tweepy

from carmen.location import LocationEncoder
from elasticsearch.exceptions import RequestError

from ingress.geocode import get_geotagger
from ingress.exceptions import InvalidMappingError
from ingress.elastic import map_tweet_to_mapping

LOG = logging.getLogger(__name__)


class StdOutListener(tweepy.StreamListener):
    """
    Simple class that provides a stream processor that logs tweet text to the console.
    """
    total_tweets = []

    def __init__(self, *args, **kwargs):
        self.geotagger = get_geotagger()
        self.tweets = []
        self.location_resolver = LocationEncoder()

        super().__init__(*args, **kwargs)

    def on_data(self, raw_data):
        """
        Event handler called whenever new data is pushed to the Tweepy Stream client.

        We clean the tweet slightly here, to ensure we have a single, non-truncated text value.

        :param raw_data: New data is passed in as a JSON document, containing a
        variety of data and metadata about the new tweet.
        """
        tweet = json.loads(raw_data)

        if tweet['truncated']:
            LOG.debug('Tweet was truncated, pulling the untruncated tweet text.')
            tweet['text'] = tweet['extended_tweet']['full_text']

        LOG.debug('Received a tweet: %s', tweet['text'])
        tweet_location = self.geotagger.resolve_tweet(tweet)

        if tweet_location:
            LOG.debug(
                '\n########################\n'
                'Identified Tweet location: %s'
                '\n########################',
                tweet_location[1]
            )
            tweet['location'] = self.location_resolver.default(tweet_location[1])

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


class ESListener(tweepy.StreamListener):
    """
    Simple class that provides a stream processor that logs tweet text to Elasticsearch.
    """

    def __init__(self, *args, **kwargs):
        self.geotagger = get_geotagger()
        self.location_resolver = LocationEncoder()

        super().__init__(*args, **kwargs)

    def on_data(self, raw_data):
        """
        Event handler called whenever new data is pushed to the Tweepy Stream client.

        We clean the tweet slightly here, to ensure we have a single, non-truncated text value.

        :param raw_data: New data is passed in as a JSON document, containing a
        variety of data and metadata about the new tweet.
        """
        LOG.debug('Received new tweet')
        tweet = json.loads(raw_data)

        if tweet['truncated']:
            LOG.debug('Tweet was truncated, pulling the untruncated tweet text.')
            tweet['text'] = tweet['extended_tweet']['full_text']

        tweet_location = self.geotagger.resolve_tweet(tweet)

        tweet['geotagged'] = False
        if tweet_location:
            LOG.debug('  This tweet includes location information')
            tweet['location'] = self.location_resolver.default(tweet_location[1])

            if 'latitude' in tweet['location']:
                tweet['coordinates'] = {
                    'lat': tweet['location']['latitude'],
                    'lon': tweet['location']['longitude'],
                }
                tweet['geotagged'] = True

        try:
            #  LOG.debug('tweet: %s', json.dumps(tweet, indent=2))
            tweet_doc = map_tweet_to_mapping(tweet)
            tweet_doc.save()
            LOG.debug('Tweet saved to ES')
        except (InvalidMappingError, RequestError) as error:
            LOG.error('Failed to ingest tweet: %s', error, exc_info=True)
            # error.info looks like this:
            #  {
            #     'error':
            #         {
            #             'root_cause':
            #                 [
            #                     {
            #                         'type': 'mapper_parsing_exception',
            #                         'reason': 'failed to parse [coordinates]'
            #                     }
            #                 ],
            # ...
            error_cause = error.info['error']['root_cause'][0]['reason']
            broken_segment = re.search(r'.+\[(.+)\]', error_cause)
            if broken_segment.groups:
                broken_segment = broken_segment.group(1)
                LOG.error('Failing segment: %s', json.dumps(tweet[broken_segment], indent=4))

            return False

        return True

    def on_exception(self, exception=None):

        print(exception)
