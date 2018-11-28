"""
This module contains wrapper code around the carmen tweet geolocation library.

The Carmen library takes JSONified tweet objects (like those returned by
tweepy) and will attempt to derive either a precise location, or a location
string (i.e. London, United Kingdom etc.).

This is the first step in getting hold of coordinates for a tweet that
correspond to approximately where the tweet originates.

The final step will be to geocode the location information returned from this
module.
"""
import logging

from carmen import get_resolver
from carmen.location import LocationEncoder

from ingress.data_processing.processing import PluginBase

LOG = logging.getLogger(__name__)


class GeoCoding(PluginBase):
    """
    Class that will attempt to geotag a tweet.
    """

    def __init__(self, *args, **kwargs):
        """
        Setup Carmen geotagging options alongside any other instance
        initialisation done by super.
        """
        resolver_options = {'place': {'allow_unknown_locations': True}}
        self.geotagger = get_resolver(options=resolver_options)
        self.geotagger.load_locations()
        self.location_resolver = LocationEncoder()

        super().__init__(*args, **kwargs)

    def process_tweet(self, tweet_json=None):
        """
        Attempt to geotag the tweet data.

        Returns the tweet with new data if any was resolved and will set
        geotagged according to success or failure.
        """
        LOG.debug('Attempting to geotag tweet')
        tweet_location = self.geotagger.resolve_tweet(tweet_json['raw'])

        tweet_json['geotagged'] = False
        if tweet_location:
            LOG.debug('  This tweet includes location information')
            tweet_json['location'] = self.location_resolver.default(tweet_location[1])

            if 'latitude' in tweet_json['location'] and 'longitude' in tweet_json['location']:
                tweet_json['coordinates'] = {
                    'lat': tweet_json['location']['latitude'],
                    'lon': tweet_json['location']['longitude'],
                }
                tweet_json['geotagged'] = True
                LOG.debug('Geotagging completed!')

        return tweet_json
