"""Unit tests for the ingress.data_processing.geocode module."""

from copy import deepcopy

import pytest

import ingress.data_processing.geocode as idg

from tests.tweets import TWEETS


@pytest.mark.parametrize(
    'input_tweet,is_geotagged,expected_coordinates',
    [
        (
            # We copy only the unprocessed piece of tweet here.
            {'_raw': deepcopy(raw_tweet['_raw'])},
            raw_tweet['geotagged'],
            raw_tweet.get('coordinates'),
        ) for raw_tweet in TWEETS
    ]
)
def test_geocode_process_tweet_happy_case(input_tweet, is_geotagged, expected_coordinates):
    """
    Verify geocoding a tweet functions correctly given valid input.

    Should return a coordinates sub-dict after processing a tweet with location data returns a
    tweet object with the appropriate fields completed or not.

    Happy case should not raise.
    """
    geocoder = idg.GeoCoding()

    processed_tweet = geocoder.process_tweet(input_tweet)

    assert processed_tweet['geotagged'] == is_geotagged
    assert processed_tweet.get('coordinates') == expected_coordinates
