"""
This module contains wrapper code around the carmen tweet geolocation library.

The Carmen library takes JSONified tweet objects (like those returned by tweepy) and will attempt to derive either a precise location, or a location string (i.e. London, United Kingdom etc.).

This is the first step in getting hold of coordinates for a tweet that correspond to approximately where the tweet originates.

The final step will be to geocode the location information returned from this module.
"""

import carmen

def get_geotagger():
    """
    Simple factory function to instantiate a carmen resolver instance.
    """
    geotagger = carmen.get_resolver()
    geotagger.load_locations()

    return geotagger

