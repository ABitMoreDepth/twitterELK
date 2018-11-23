"""
Simple module to contain data queue used as an intermediary between ingress and
processing of tweets.
"""

from queue import Queue

DATA_QUEUE = Queue()
