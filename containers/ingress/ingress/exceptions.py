"""Collection of custom exception classes used throughout the ingress code."""


class InvalidMappingError(Exception):
    """Custom exception indicating failure to serialise a tweet to elasticsearch document."""
