"""
Collection of custom exception classes used throughout the ingress code.
"""


class InvalidMappingError(Exception):
    """
    Exception class used to indicate issues when attempting to serialise a
    processed tweet dict into an ES Tweet instance.
    """
    pass
