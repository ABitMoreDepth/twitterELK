"""
Container module which provides various data structures and globally useful systems.
"""
import weakref

import tweepy

from ingress.data_processing.processing import DataProcessor

_API_CACHE = weakref.WeakValueDictionary()
_PROCESSOR_CACHE = weakref.WeakValueDictionary()


def get_api_instance(name, *args, **kwargs):
    """ Factory that produces a cached Tweepy Stream instance.
    """
    if name not in _API_CACHE:
        api = tweepy.Stream(*args, **kwargs)
        _API_CACHE[name] = api
    else:
        api = _API_CACHE[name]

    return api


def get_processor_instance(name, *args, **kwargs):
    """ Factory that produces a cached DataProcessor instance.
    """
    if name not in _API_CACHE:
        processor = DataProcessor(*args, **kwargs)
        _PROCESSOR_CACHE[name] = processor
    else:
        processor = _PROCESSOR_CACHE[name]

    return processor


