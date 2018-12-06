"""Unit tests for the ingress.data_processing.sentiment module."""

from unittest.mock import create_autospec
from collections import namedtuple
from pprint import pformat

import pytest
import textblob.download_corpora as td
from textblob import TextBlob

import ingress.data_processing.sentiment as ids


@pytest.mark.parametrize(
    'input_tweet',
    [
        {
            '_raw': {
                'text': 'Hello, world!',
                'truncated': False,
                'lang': 'en',
            }
        },
        {
            '_raw':
                {
                    'text': 'Hello, world!',
                    'extended_tweet': {
                        'full_text': 'Hello, world!',
                    },
                    'truncated': True,
                    'lang': 'en',
                }
        },
        {},
    ],
)
def test_process_tweet_happy_case(input_tweet, monkeypatch):
    """Verify the sentiment analysis processor will return the appropriate data structures."""
    mock_download_all = create_autospec(td.download_all)
    monkeypatch.setattr('ingress.data_processing.sentiment.text_blob_download', mock_download_all)

    mock_text = 'Hello, World!'
    mock_text_blob = create_autospec(TextBlob)
    mock_text_blob(mock_text).__len__.return_value = len(mock_text)
    mock_sentiment = namedtuple('sentiment', ['polarity', 'subjectivity'])
    mock_text_blob(mock_text).sentiment = mock_sentiment(0, 0)
    mock_text_blob(mock_text).words = []
    monkeypatch.setattr('ingress.data_processing.sentiment.TextBlob', mock_text_blob)

    sentiment_analysis = ids.SentimentAnalysis()

    processed_data = sentiment_analysis.process_tweet(input_tweet)
    print('Input Tweet:\n{}'.format(pformat(input_tweet, indent=4)))
    print('Processed Tweet:\n{}'.format(pformat(processed_data, indent=4)))
    if input_tweet:
        assert processed_data['text']['pattern_polarity'] == 0
        assert processed_data['text']['pattern_subjectivity'] == 0
        assert processed_data['text']['tweet_length'] == 0
    else:
        assert processed_data == input_tweet
