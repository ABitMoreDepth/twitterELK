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
import inspect
import logging
import queue
import sys
import typing

from importlib import import_module
from os import walk
from os.path import join, dirname
#  from os.path import sep as os_separator

from ingress.data_queue import DATA_QUEUE
from ingress.elastic import map_tweet_to_mapping

LOG = logging.getLogger(__name__)

TypeVar = typing.TypeVar('TypeVar', bound=typing.Type)


def find_subclasses(cls: TypeVar) -> typing.Generator[TypeVar, None, None]:
    """
        Recursively returns all subclasses of the given class.
    """
    if not inspect.isclass(cls):
        raise TypeError('cls must be a valid class: {}'.format(cls))

    for class_ in cls.__subclasses__():
        yield class_
        for return_value in find_subclasses(class_):
            yield return_value


class PluginBase:
    """
    Base class for data analysis code.  Any code inheriting from this class
    should overwrite the _process_order value in order to be executed at the
    proper time in the processing cycle.
    """
    process_order = 100

    def process_tweet(self, tweet_json=None):
        """
        Stub method to be overwritten by subclasses, should either return a
        JSON-compatible object, or return None to indicate completion of the
        processing chain.
        """
        raise NotImplementedError

    @staticmethod
    def import_subclasses():
        """
        Iterate through plugins directory and attempt to load in any plugin
        files.  Plugin files are located in the data_processing directory and
        are python files aside from processing.py.
        """
        for _, _, file_names in walk(join(dirname(__file__))):
            for file_name in file_names:
                if (file_name.endswith('.py') and not file_name.startswith('processing')
                        and not file_name.startswith('__')):
                    module_path = 'ingress.data_processing.{}'.format(file_name).rstrip('.py')
                    if module_path not in sys.modules:
                        try:
                            LOG.debug('attempting to import: %s', module_path)
                            import_module(module_path)
                        except ImportError as error:
                            LOG.error(str(error), exc_info=True)


class DataProcessor:
    """
    Wrapper class which consumes from the DATA_QUEUE and applies any processing
    plugins to the pulled data.
    """

    def __init__(self):
        self.running = False
        self.data = None
        self.plugins = []

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
        tweet_doc = map_tweet_to_mapping(self.data)
        tweet_doc.save()
