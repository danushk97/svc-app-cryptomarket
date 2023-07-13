"""
This module provides the function that provides logger.
"""

from os import environ
import logging

from src.constants import Constants


def get_logger(name: str):
    logger = logging.getLogger(name)
    level = logging.INFO
    if environ.get(Constants.LOGGING_LEVEL) == Constants.DEBUG:
        level = logging.DEBUG
    
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    return logger
