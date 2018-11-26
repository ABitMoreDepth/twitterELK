"""
Container module which provides various data structures and globally useful systems.
"""
import weakref


_SINGLETON_CACHE = weakref.WeakValueDictionary()


def get_singleton_instance(obj_type, *args, **kwargs):
    """ Factory that produces a cached Tweepy Stream instance.
    """
    if obj_type not in _SINGLETON_CACHE:
        object_instance = obj_type(*args, **kwargs)
        _SINGLETON_CACHE[obj_type] = object_instance
    else:
        object_instance = _SINGLETON_CACHE[obj_type]

    return object_instance
