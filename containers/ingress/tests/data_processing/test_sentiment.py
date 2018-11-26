"""
Unit tests for the ingress.data_processing.sentiment module.
"""

from unittest.mock import create_autospec
from collections import namedtuple
from pprint import pformat

import pytest
import textblob.download_corpora as td
from textblob import TextBlob

import ingress.data_processing.sentiment as ids

from tests.tweets import TWEET_PARSE_SAMPLES


@pytest.mark.parametrize(
    'input_tweet',
    [
        {
            'text': 'Hello, world!',
            'truncated': False,
        },
        {
            'text': 'Hello, world!',
            'extended_tweet': {
                'full_text': 'Hello, world!',
            },
            'truncated': True
        },
        {},
    ],
)
def test_process_tweet_happy_case(input_tweet, monkeypatch):
    """
    Verify that when given reasonable data, the sentiment analysis processor will return the appropriate data structure.
    """
    mock_download_all = create_autospec(td.download_all)
    monkeypatch.setattr('ingress.data_processing.sentiment.td.download_all', mock_download_all)

    mock_text_blob = create_autospec(TextBlob)
    mock_sentiment = namedtuple('sentiment', ['polarity', 'subjectivity'])
    mock_text_blob(input_tweet.get('text')).sentiment = mock_sentiment(0, 0)
    mock_text_blob(input_tweet.get('text')).words = []
    monkeypatch.setattr('ingress.data_processing.sentiment.TextBlob', mock_text_blob)

    sa = ids.SentimentAnalysis()

    processed_data = sa.process_tweet(input_tweet)
    print('Input Tweet:\n{}'.format(pformat(input_tweet, indent=4)))
    print('Processed Tweet:\n{}'.format(pformat(processed_data, indent=4)))
    if input_tweet:
        assert processed_data['sentiment_polarity'] == 0
        assert processed_data['sentiment_subjectivity'] == 0
        assert processed_data['tweet_length'] == 0
    else:
        assert processed_data == input_tweet
