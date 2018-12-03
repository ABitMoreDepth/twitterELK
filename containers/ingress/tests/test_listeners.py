"""
Unit tests for the ingress.listeners module.
"""
import json

import pytest

import ingress.listeners as il
from ingress.structures import DATA_QUEUE


def test_listener_queue_push_happy():
    """
    Verify that new items are in fact put on the queue when given valid JSON data.
    """
    listener = il.QueueListener()

    sample_data = {'key': 'hello, world!'}

    listener.on_data(json.dumps(sample_data))
    assert DATA_QUEUE.not_empty
    assert DATA_QUEUE.qsize() == 1
    assert DATA_QUEUE.get() == sample_data


@pytest.mark.parametrize(
    'input_data',
    [
        None,
        '',
        '{lkj',
    ],
)
def test_listener_queue_push_bad_data(input_data, caplog):
    """
    Verify that the listener handles poor data appropriately.
    """
    listener = il.QueueListener()

    listener.on_data(input_data)

    assert 'Encountered issue attempting to parse new data.' in caplog.text
