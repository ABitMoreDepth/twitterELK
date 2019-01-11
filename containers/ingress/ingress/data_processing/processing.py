"""
Module containing the base DataProcessor class.

The DataProcessor includes a blocking loop consuming
ingress.data_queue.DATA_QUEUE items, eventually resulting in fully processed
documents being submitted to elasticsearch.

The implementation here takes heavy inspiration from Mike Auty's plugins
pattern, which itself is derived from python's object __subclass__ magic.

The core concept is that we have a plugin base class, from which any plugin may
inherit, which is used from the base class down to handle data analysis
extensions, rather than the more traditional mess of importing loads of stuff
and then registering individual instances of various classes, which is
difficult to make properly extensible without munging around in the
application.

Credit to Mike Auty for the intial concept surrounding __subclasses__ and some
sample code that makes this pattern viable.
"""

import logging
from queue import Queue, Empty
from typing import Any, Dict, List, cast

import elasticsearch_dsl as es

from ingress.utils import find_subclasses
from ingress.structures import PluginBase

LOG = logging.getLogger(__name__)


class DataProcessor:
    """
    Worker class that processes data from DATA_QUEUE.

    Data is pushed to DATA_QUEUE by other threads (the Tweepy listener).  This
    class provides an interruptable, blocking call that will consume from the
    list and apply any processing plugins to the pulled data.
    """

    def __init__(self, twitter_index: str, queue: Queue) -> None:
        """Setup various instance variables for later use."""
        self.running = False
        #  self.data: Dict[str, Any] = {}
        self.plugins: List[PluginBase] = []
        self.twitter_index = twitter_index
        self.queue = queue

    def _load_plugins(self):
        """Load any processing plugins provided.

        Iterates through any subclasses of the PluginBase class and loads a
        list of plugin instances into self.plugins for use elsewhere in the
        class.
        """
        self.plugins = sorted(
            [plugin() for plugin in find_subclasses(PluginBase)],
            key=lambda plugin: plugin.process_order,
        )
        LOG.debug('Loaded processing plugins: %s', self.plugins)

    def start(self) -> None:
        """Start the processing loop."""
        LOG.info('Beginning DataProcessor')
        self.running = True
        self.retrieve_data()

    def stop(self) -> None:
        """Stop the processing loop."""
        self.running = False

    def retrieve_data(self, timeout=0.01) -> None:
        """
        Pull data from the queue.

        Sit in a loop and block the current thread whilst waiting for data to
        get pushed into the queue.  This can be cancelled by setting the
        DataProcessor instance's running attribute to false.
        """
        while self.running:
            try:
                data: Dict[str, Any] = cast(Dict[str, Any], self.queue.get(timeout=timeout))
                LOG.debug('Retrieved new data from the queue to process.')

                self.process_data(data)
            except Empty:
                continue

    def process_data(self, data: Dict[str, Any]) -> None:
        """
        Iterate through all identified plugins and process tweet data accordingly.

        Will attempt to store the data when processing is complete.
        """
        if not self.plugins:
            self._load_plugins()

        for plugin in self.plugins:
            LOG.debug('Processing data with %s plugin.', plugin)
            #  self.data = plugin.process_tweet(self.data)
            data = cast(Dict[str, Any], plugin.process_tweet(data))

        if data:
            LOG.debug('Attempting to store data')
            self.store_data(data)
            LOG.debug('Data successfully stored')

    def store_data(self, data: Dict[str, Any]) -> None:
        """Attempt to store the data into Elasticsearch."""
        es_connection = es.connections.get_connection()
        es_connection.create(
            body=data,
            doc_type='doc',
            id=data['_raw']['id_str'],
            index=self.twitter_index,
        )
