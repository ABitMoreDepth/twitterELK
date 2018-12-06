"""Unit tests for the ingress.listeners module."""
import json

import arrow
import pytest

import ingress.listeners as il
from ingress.structures import DATA_QUEUE


def test_listener_queue_push_happy():
    """Verify that new items are in fact put on the queue when given valid JSON data."""
    listener = il.QueueListener()

    time = arrow.get('2018-12-25T23:59:59.0+00:00')  # Deliberately not epoch
    # Twitter for some reason gives us time since epoch in miliseconds, whilst
    # Arrow works off of time in seconds when given an integer, hence the
    # division by 1000 both here and in the application code.
    sample_data = {'timestamp_ms': time.timestamp * 1000, '_raw': {'key': 'hello, world!'}}

    expected_data = {'_raw': sample_data, 'timestamp': time.datetime}

    listener.on_data(json.dumps(sample_data))
    assert DATA_QUEUE.qsize() == 1
    assert DATA_QUEUE.get() == expected_data


@pytest.mark.parametrize(
    'input_data',
    [
        None,
        '',
        '{lkj',
    ],
)
def test_listener_queue_push_bad_data(input_data, caplog):
    """Verify that the listener handles poor data appropriately."""
    listener = il.QueueListener()

    listener.on_data(input_data)

    assert 'Encountered issue attempting to parse new data.' in caplog.text
