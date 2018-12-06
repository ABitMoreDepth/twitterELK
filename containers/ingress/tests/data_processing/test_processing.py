"""Unit tests for the ingress.data_processing.processing module."""

from copy import deepcopy
from queue import Queue
from unittest.mock import create_autospec

import ingress.data_processing.processing as idp


def test_data_processor_start(monkeypatch):
    """Assert that the DataProcessor.start method sets the running flag to True."""
    mock_retrieve_data = create_autospec(idp.DataProcessor.retrieve_data)
    monkeypatch.setattr(
        'ingress.data_processing.processing.DataProcessor.retrieve_data',
        mock_retrieve_data
    )

    data_processor = idp.DataProcessor('', Queue())

    data_processor.start()

    assert data_processor.running is True


def test_data_processor_stop():
    """Assert that the DataProcessor.stop method sets the running flag to False."""
    data_processor = idp.DataProcessor('', Queue())
    data_processor.running = True
    data_processor.stop()

    assert data_processor.running is False


def test_data_processor_retrieve_data_stops(monkeypatch):
    """Verify DataProcessor.process_data correctly pulls data from a queue."""
    stop = False
    sample = {'sample': 'Hello, World!'}
    sample_data = [None, deepcopy(sample), deepcopy(sample), deepcopy(sample)]
    called_values = []

    def mock_process_data(self, data):
        """Mocked process_data that passes input parameters back to test case."""
        nonlocal called_values
        nonlocal stop

        if stop:
            self.stop()
        else:
            called_values.append(data)

    monkeypatch.setattr(
        'ingress.data_processing.processing.DataProcessor.process_data',
        mock_process_data
    )

    queue = create_autospec(Queue(), instance=True)

    sample_gen_data = (item for item in sample_data)

    def mock_queue_get(*_, **__):
        """Mock Queue.get method.

        Allows us to control what data is returned, and to control when to
        close the retrieve_data loop.
        """
        nonlocal sample_gen_data
        nonlocal stop

        data = None

        try:
            data = next(sample_gen_data)
        except StopIteration:
            stop = True

        return data

    queue.get = mock_queue_get

    data_processor = idp.DataProcessor(twitter_index='', queue=queue)
    data_processor.running = True
    data_processor.retrieve_data()

    # We end up back here because our mocked process_data function will stop
    # the DataProcessor once its run through a set of calls.
    assert data_processor.running is False
    assert called_values == sample_data


def test_data_processor_process_data(monkeypatch):
    """Verify the behaviour of the DataProcessor.process_data method."""
    called_data = []

    class MockPlugin(idp.PluginBase):
        """Noddy plugin class we can use to verify the DataProcessor class's behaviour."""

        nonlocal called_data

        def process_tweet(self, data):
            """Mock process_tweet method we can use to verify DataProcessor behaviour."""
            nonlocal called_data
            called_data.append(data)

            return data

    def mock_load_plugins(self):
        """Mock of DataProcessor._load_plugins."""
        nonlocal MockPlugin
        self.plugins = [MockPlugin()]

    monkeypatch.setattr(
        'ingress.data_processing.processing.DataProcessor._load_plugins',
        mock_load_plugins
    )

    mock_store_data = create_autospec(idp.DataProcessor.store_data)
    monkeypatch.setattr(
        'ingress.data_processing.processing.DataProcessor.store_data',
        mock_store_data
    )

    sample = {'sample': 'hello, world!'}
    data_processor = idp.DataProcessor('', None)

    data_processor.process_data(None)
    data_processor.process_data(sample)
    data_processor.process_data(sample)

    assert called_data == [None, sample, sample]
