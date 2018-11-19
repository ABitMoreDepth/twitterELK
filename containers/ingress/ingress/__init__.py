""" Initial setup for the ingress package.  Includes base logging setup and
Elasticsearch connection establishment.
"""

import logging
from os import getenv

from ingress.elastic import setup_mappings

__version__ = '0.0.1'

# Setup logging for the package.  We check here whether the user has overridden
# the default log level.

LOG_FORMAT = (
    "%(asctime)s %(levelname)s %(thread)d - [%(module)s:%(lineno)s] (%(funcName)s):  %(message)s"
)


def config_logging(level='INFO'):
    """ Noddy function that will attempt to configure logging to the user desired level

    :param level: The log level name to which we should attempt to log at.
    """
    try:
        if level == 'SILLY':
            # Make everything log at debug level
            logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
            root_logger = logging.getLogger()
            root_logger.setLevel(logging.DEBUG)
            root_logger.debug(
                'Configured root logger to DEBUG, every library should log verbosely'
            )
        else:
            logging.basicConfig(format=LOG_FORMAT, level=logging.ERROR)

            log = logging.getLogger(__name__)
            log.setLevel(level)
            log.debug('Configured logging to level %s', level)

    except AttributeError:
        # Default case here when user borks setting the level.
        logging.basicConfig(format=LOG_FORMAT, level=getattr(logging, level))

        log = logging.getLogger(__file__)
        log.error('User attempted to set an invalid log level, defaulting to INFO')


config_logging(getenv("LOG_LEVEL", "INFO"))
setup_mappings(getenv("ES_HOST"))
