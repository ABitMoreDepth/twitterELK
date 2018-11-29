"""
Container module which provides various data structures and globally useful systems.
"""
import weakref
import logging


LOG = logging.getLogger(__name__)
_SINGLETON_CACHE = weakref.WeakValueDictionary()


def get_singleton_instance(obj_type, *args, **kwargs):
    """ Factory that produces a cached Tweepy Stream instance.
    """
    LOG.debug('Attempting to retrieve cached %s', obj_type)
    if obj_type not in _SINGLETON_CACHE:
        LOG.debug('%s not found, instantiating new instance', obj_type)
        object_instance = obj_type(*args, **kwargs)
        _SINGLETON_CACHE[obj_type] = object_instance
    else:
        LOG.debug('%s found, returning cached instance', obj_type)
        object_instance = _SINGLETON_CACHE[obj_type]

    return object_instance
