"""
This module contains storage routines used to persist tweets.
"""

import logging

import arrow
from elasticsearch_dsl import (
    Boolean,
    Date,
    Document,
    InnerDoc,
    Nested,
    Text,
)
from elasticsearch_dsl.document import DocumentMeta

from ingress.exceptions import InvalidMappingError

LOG = logging.getLogger(__name__)


class User(InnerDoc):
    """
    InnerDoc mapping of user data embedded within a tweet.
    """
    ingress_mapping = {
        'id': 'user/id',
        'location': 'user/location',
        'description': 'user/description',
        'geo_enabled': 'user/geo_enabled',
        'lang': 'user/lang'
    }
    id = Text()
    location = Text()
    description = Text()
    geo_enabled = Boolean()
    lang = Text()


class Location(InnerDoc):
    """
    InnerDoc mapping of location information embedded within a tweet (This
    data is created by us during the processing pipeline).
    """
    ingress_mapping = {
        'country': 'location/country',
        'state': 'location/state',
        'county': 'location/county',
        'city': 'location/city',
        'id': 'location/id',
        'latitude': 'location/latitude',
        'longitude': 'location/longitude',
        'resolution_method': 'location/resolution_method'
    }
    country = Text()
    state = Text()
    county = Text()
    city = Text()
    id = Text()
    latitude = Text()
    longitude = Text()
    resolution_method = Text()


class Tweet(Document):
    """
    Elasticsearch Document mapping to store tweets.
    """
    ingress_mapping = {
        'id':
            'id_str',
        'created_at':
            'created_at',
        'text':
            'text',
        'truncated':
            'truncated',
        'user':
            User,
        'geo':
            'geo',
        'coordinates':
            'coordinates',
        'place':
            'place',
        'full_text':
            'extended_tweet/full_text',
        'hashtags':
            (
                lambda tag_list: [tag.get('text') for tag in tag_list],
                'extended_tweet/entities/hashtags',
            ),
        'lang':
            'lang',
        'timestamp_ms': (
            lambda x: arrow.get(int(x) / 1000).datetime,
            'timestamp_ms',
        ),
        'location':
            Location
    }
    id = Text()
    created_at = Text()
    text = Text()
    truncated = Boolean()
    user = Nested(User)
    geo = Text()
    coordinates = Text()
    place = Text()
    full_text = Text()
    hashtags = Text(multi=True)
    lang = Text()
    timestamp = Date()
    location = Nested(Location)


def map_tweet_to_mapping(tweet=None, tweet_doc=None, ingress_mapping=Tweet.ingress_mapping):
    """
    Routine which will attempt to parse a tweet object and return an ES Tweet
    Document, which can be saved to the database.

    This function uses the ingress_mapping variable to dynamically process a
    tweet.  Updating the class and that mapping should be sufficient to adjust
    the serialisation of tweets into Elasticsearch.

    NOTE: The ingress mapping defines a series of key:value pairs, where the
    key must be one of the Tweet classes attributes.  The value may be one of
    the following:
    - a simple string: This will result in pulling a top level attribute out of
      the tweet data
    - a / delimited path: This will descend into nested dict objects to pull
      out a value from the tweet data, handy when flattening the data out.
    - a tuple of a callable and one of the above to options: This will first
      perform the above operation(s), then execute the callable on the result.
      This allows you to define a transformation as part of the ingress
      mapping.  This is helpful for transforming epoch time into a python date
      time, for instance.
    - an InnderDoc class: This will call map_tweet_to_mapping to process the
      nested document and merge the results into the outer document.

    :param tweet: Tweet object post processing.
    :param tweet_doc: Tweet Document instance to amend, used when dealing with
    nested data, can also be used to update the values of an existing document,
    rather than create a new one.
    :param ingress_mapping: The mapping to use when serialising a tweet,
    defaults to the Tweet ES classes ingress_mapping value.
    :return: Tweet class instance representing pared down tweet data.
    :raises InvalidMappingError: When unable to translate tweet data to a Tweet
    instance.
    """
    if tweet is None:
        raise InvalidMappingError

    # Initialise a new Tweet document if one hasn't been passed in.
    if tweet_doc is None:
        tweet_doc = Tweet()


    try:
        for key, value in ingress_mapping.items():
            func = None
            if isinstance(value, tuple):
                func, value = value

            LOG.debug(value)
            #  import ipdb
            #  ipdb.set_trace()
            if isinstance(value, DocumentMeta):
                # Nested doc in ingress mapping
                LOG.debug('Recursing to parse nested document: %s', value)
                sub_doc = map_tweet_to_mapping(tweet, value(), value.ingress_mapping)

                setattr(tweet_doc, key, sub_doc)
                # There's no need to further process when working with a
                # sub-document
                continue

            if not isinstance(value, str):
                raise InvalidMappingError(
                    'Improper ingress mapping detected, trying to process: {}'.format(value)
                )

            # Get a list of paths through the tweet object from which to
            # retrieve data
            data_path = value.split('/')

            data_item = tweet
            for segment in data_path:
                data_item = data_item.get(segment, None)
                if data_item is None:
                    break

            if func is not None:
                data_item = func(data_item)

            setattr(tweet_doc, key, data_item)

        return tweet_doc

    except AttributeError as exception:
        LOG.error(exception, exc_info=True)
        raise InvalidMappingError from exception
