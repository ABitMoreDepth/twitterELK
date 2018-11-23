"""
This module contains storage routines used to persist tweets.
"""

import logging

import arrow
from elasticsearch_dsl import (
    Boolean,
    Date,
    Document,
    GeoPoint,
    Index,
    InnerDoc,
    Keyword,
    Object,
    Text,
)
from elasticsearch_dsl.connections import connections
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
    country = Keyword(doc_values=True)
    state = Keyword(doc_values=True)
    county = Keyword(doc_values=True)
    city = Keyword(doc_values=True)
    id = Text()
    latitude = Text()
    longitude = Text()
    resolution_method = Text()


class Place(InnerDoc):
    """
    InnerDoc mapping of Twitter Place information embedded within a tweet.

    Sample data:
    "place": {
        "id": "44cfc67a4237cb80",
        "url": "https://api.twitter.com/1.1/geo/id/44cfc67a4237cb80.json",
        "place_type": "city",
        "name": "Catshill",
        "full_name": "Catshill, England",
        "country_code": "GB",
        "country": "United Kingdom",
        "bounding_box": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -2.069936,
                        52.355344
                    ],
                    [
                        -2.069936,
                        52.372085
                    ],
                    [
                        -2.034409,
                        52.372085
                    ],
                    [
                        -2.034409,
                        52.355344
                    ]
                ]
            ]
        },
        "attributes": {}
      }
    """
    ingress_mapping = {
        'id': 'place/id',
        'url': 'place/url',
        'place_type': 'place/place_type',
        'name': 'place/name',
        'full_name': 'place/full_name',
        'country_code': 'place/country_code',
        'country': 'place/country',
        'bounding_box': 'place/bounding_box',
        'attributes': 'place/attributes'
    }

    id = Text()
    url = Text()
    place_type = Text()
    name = Text()
    full_name = Text()
    country_code = Text()
    country = Text()
    bounding_box = Object(dynamic=True)
    attributes = Object(dynamic=True)


class Tweet(Document):
    """
    Elasticsearch Document mapping to store tweets.
    """
    ingress_mapping = {
        'coordinates': 'coordinates',
        'created_at': 'created_at',
        'geo': 'geo',
        'geotagged': (
            lambda geo_tag: False if geo_tag is None else geo_tag,
            'geotagged',
        ),
        'hashtags':
            (
                lambda tag_list: [tag.get('text') for tag in tag_list],
                'entities/hashtags',
            ),
        'id': 'id_str',
        'place': Place,
        'text': 'text',
        'user': User,
        'lang': 'lang',
        'location': Location,
        'timestamp': (
            lambda x: arrow.get(int(x) / 1000).datetime,
            'timestamp_ms',
        ),
    }
    id = Text()
    created_at = Text()
    text = Text()
    truncated = Boolean()
    user = Object(User)
    geo = Object(dynamic=True)
    geotagged = Boolean()
    coordinates = GeoPoint()
    place = Object(Place)
    full_text = Text()
    hashtags = Text(multi=True)
    lang = Keyword(doc_values=True)
    timestamp = Date()
    location = Object(Location)

    class Index:  # pylint: disable=too-few-public-methods
        """Simple class used to define the index settings for the mapping."""
        name = 'tweets'
        settings = {'number_of_shards': 1}


def map_tweet_to_mapping(tweet=None, tweet_doc=None, ingress_mapping=Tweet.ingress_mapping):
    """
    Attempt to parse a tweet object and return an ES Tweet
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

            #  LOG.debug(value)
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
                if data_item is None or data_item == 'null':
                    break

            if func is not None and data_item is not None:
                data_item = func(data_item)

            setattr(tweet_doc, key, data_item)

        LOG.debug('Parsed tweet: %s', tweet_doc.to_dict())
        return tweet_doc

    except AttributeError as exception:
        LOG.error(exception, exc_info=True)
        raise InvalidMappingError from exception


def setup_mappings(es_host=None):
    """
    Run through the initial setup of the elasticsearch index used to store tweets.
    """
    if es_host is None:
        LOG.warning('No Elasticsearch connection setup')
        return

    connections.create_connection(hosts=[es_host])

    tweet_index = Index('tweets')
    if not tweet_index.exists():
        Tweet.init()
