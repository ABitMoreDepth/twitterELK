"""Container module which provides various data structures and globally useful systems."""

import logging
from typing import Any, Dict, Mapping, Union
import sys
#  import weakref

from importlib import import_module
from os import walk
from os.path import join, dirname, normpath
from queue import Queue

LOG = logging.getLogger(__name__)
#  SINGLETON_CACHE: Dict = weakref.WeakValueDictionary()
SINGLETON_CACHE: Dict = dict()
DATA_QUEUE: Queue = Queue()


class PluginBase:
    """
    Base class for data analysis code.

    Any code inheriting from this class should overwrite the _process_order
    value in order to be executed at the proper time in the processing cycle.
    """

    process_order: int = 100
    data_schema: Mapping = {}

    def process_tweet(self, tweet_json: Dict[str, Any]) -> Union[Dict[str, Any], None]:
        """
        Stub method to be overwritten by subclasses.

        Should either return a JSON-compatible object, or return None to
        indicate completion of the processing chain.
        """
        raise NotImplementedError

    @staticmethod
    def import_subclasses() -> None:
        """
        Iterate through plugins directory and attempt to load in any plugin files.

        Plugin files are located in the data_processing directory and
        are python files aside from processing.py.
        """
        plugin_path = normpath(join(dirname(__file__), 'data_processing'))
        LOG.debug('Plugin Directory located at: %s', plugin_path)
        for _, _, file_names in walk(plugin_path):
            for file_name in file_names:
                LOG.debug('Processing file: %s', file_name)
                if all((
                        file_name.endswith('.py'),
                        not file_name.startswith('processing'),
                        not file_name.startswith('__'),
                        # Shouldn't be needed in prod, dev sometimes includes
                        # linter partials containing @'s
                        '@' not in file_name,
                )):
                    module_path = 'ingress.data_processing.{}'.format(file_name).rstrip('.py')
                    LOG.debug('%s in sys.modules? -> %s', module_path, module_path in sys.modules)
                    if module_path not in sys.modules:
                        try:
                            LOG.debug('attempting to import: %s', module_path)
                            import_module(module_path)
                        except ImportError as error:
                            LOG.error(str(error), exc_info=True)
