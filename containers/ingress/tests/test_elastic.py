"""
Unit tests for the ingress.elastic module.
"""

import logging

import arrow
import pytest

import ingress.elastic as ie
from ingress.exceptions import InvalidMappingError

from tests.tweets import TWEET_PARSE_SAMPLES

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


@pytest.mark.parametrize(
    'tweet,tweet_doc,ingress_mapping',
    [
        (None,
         None,
         None),
        ({},
         None,
         None),
        ({},
         {},
         None),
    ],
)
def test_raise_invalid_mapping_error_on_tweet_map(tweet, tweet_doc, ingress_mapping):
    with pytest.raises(InvalidMappingError):
        ie.map_tweet_to_mapping(
            tweet=tweet,
            tweet_doc=tweet_doc,
            ingress_mapping=ingress_mapping,
        )


@pytest.mark.parametrize(
    'tweet,tweet_doc,ingress_mapping,expected_result',
    [
        (
            tweet_data[0],
            None,
            ie.Tweet.ingress_mapping,
            tweet_data[1],
        ) for tweet_data in TWEET_PARSE_SAMPLES
    ],
)
def test_map_tweet_to_mapping_happy_case_all_data(
        tweet,
        tweet_doc,
        ingress_mapping,
        expected_result,
):
    mapped_tweet = ie.map_tweet_to_mapping(
        tweet=tweet,
        tweet_doc=tweet_doc,
        ingress_mapping=ingress_mapping,
    )
    for key in ingress_mapping.keys():
        mapped_key = getattr(mapped_tweet, key)
        expected_key = getattr(expected_result, key)
        LOG.info(
            'Comparing %s field of expected vs mapped tweet: %s == %s',
            key,
            expected_key,
            mapped_key,
        )
        assert mapped_key == expected_key


def test_mapping_tweet_raises_invalid_mapping_error_non_str_mapping():

    class DummyTweetDoc:
        ingress_mapping = {'sample_invalid_mapping': 1234}

    with pytest.raises(InvalidMappingError):
        ie.map_tweet_to_mapping(
            tweet='',
            tweet_doc=DummyTweetDoc(),
            ingress_mapping=DummyTweetDoc.ingress_mapping
        )
