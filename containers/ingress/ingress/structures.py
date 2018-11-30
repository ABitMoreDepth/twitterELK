"""
Container module which provides various data structures and globally useful systems.
"""
import logging
import sys
#  import weakref

from importlib import import_module
from os import walk
from os.path import join, dirname, normpath

#  import elasticsearch_dsl as es


LOG = logging.getLogger(__name__)
#  SINGLETON_CACHE = weakref.WeakValueDictionary()
SINGLETON_CACHE = dict()


class PluginBase:
    """
    Base class for data analysis code.  Any code inheriting from this class
    should overwrite the _process_order value in order to be executed at the
    proper time in the processing cycle.
    """
    process_order = 100
    data_schema = {}

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
        plugin_path = normpath(join(dirname(__file__), 'data_processing'))
        LOG.debug('Plugin Directory located at: %s', plugin_path)
        for _, _, file_names in walk(plugin_path):
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
