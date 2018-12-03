"""
Module containing the base Processing class, which includes a blocking loop
consuming ingress.data_queue.DATA_QUEUE items, eventually resulting in fully
processed documents being submitted to elasticsearch.

The implementation here takes heavy inspiration from Mike Auty's plugins
pattern, which itself is derived from python's object __subclass__ magic.

The core concept is that we have a plugin base class, from which any plugin may
inherit, which is used from the base class down to handle data analysis
extensions, rather than the more traditional mess of importing loads of stuff
and then registering individual instances of various classes, which is
difficult to make properly extensible without munging around in the
application.

Credit to Mark Auty for the intial concept surrounding __subclasses__ and some
sample code that makes this pattern viable.
"""
import logging
import queue

import elasticsearch_dsl as es

from ingress.helpers import find_subclasses
from ingress.structures import DATA_QUEUE, PluginBase

LOG = logging.getLogger(__name__)


class DataProcessor:
    """
    Wrapper class which consumes from the DATA_QUEUE and applies any processing
    plugins to the pulled data.
    """

    def __init__(self, twitter_index):
        self.running = False
        self.data = None
        self.plugins = []
        self.twitter_index = twitter_index

    def start(self):
        """
        Start the processing loop.
        """
        LOG.info('Beginning DataProcessor')
        self.running = True
        self.retrieve_data()

    def stop(self):
        """
        Stop the processing loop.
        """
        self.running = False

    def retrieve_data(self, timeout=0.01):
        """
        Sit in a loop and block the current thread whilst waiting for data to
        get pushed into the queue.  This can be cancelled by setting the
        DataProcessor instance's running attribute to false.
        """
        while self.running:
            try:
                self.data = DATA_QUEUE.get(timeout=timeout)
                LOG.debug('Retrieved new data from the queue to process.')
                if self.data is not None:
                    self.process_data()
            except queue.Empty:
                continue

    def process_data(self):
        """
        Iterate through all identified plugins and process tweet data
        accordingly.

        Will attempt to store the data when processing is complete.
        """
        if not self.plugins:
            self.plugins = sorted(
                [plugin() for plugin in find_subclasses(PluginBase)],
                key=lambda plugin: plugin.process_order,
            )
            LOG.debug('Loaded processing plugins: %s', self.plugins)

        for plugin in self.plugins:
            LOG.debug('Processing data with %s plugin.', plugin)
            self.data = plugin.process_tweet(self.data)

        if self.data:
            LOG.debug('Attempting to store data')
            self.store_data()
            LOG.debug('Data successfully stored')

    def store_data(self):
        """
        Attempt to store the data into Elasticsearch.
        """
        es_connection = es.connections.get_connection()
        es_connection.create(
            body=self.data,
            doc_type='doc',
            id=self.data['_raw']['id_str'],
            index=self.twitter_index,
        )
