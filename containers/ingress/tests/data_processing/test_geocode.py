"""
Unit tests for the ingress.data_processing.geocode module.
"""

import pytest

import ingress.data_processing.geocode as idg

from tests.tweets import TWEET_PARSE_SAMPLES


@pytest.mark.parametrize(
    'input_tweet,is_geotagged,expected_coordinates',
    [
        (raw_tweet,
         tweet_doc.geotagged,
         tweet_doc.coordinates) for raw_tweet,
        tweet_doc in TWEET_PARSE_SAMPLES
    ]
)
def test_geocode_process_tweet_happy_case(input_tweet, is_geotagged, expected_coordinates):
    """
    Verify that processing a tweet with or without location data returns a
    tweet object with the appropriate fields completed or not.

    Happy case should not raise.

    """
    geocoder = idg.GeoCoding()

    processed_tweet = geocoder.process_tweet(input_tweet)

    assert processed_tweet['geotagged'] == is_geotagged
    assert processed_tweet['coordinates'] == expected_coordinates
