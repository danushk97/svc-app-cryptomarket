"""
This module provides the function that provides logger.
"""

from os import environ
import logging

from src.constants import Constants


def get_logger(name: str) -> logging.Logger:
    """
    Returns Logger instanace which can be use log.

    Args:
        name (str): A name for logger.
    
    Returns:
        logging.Logger: A Logger instance that can used to log messages.
    """
    logger = logging.getLogger(name)
    level = logging.INFO
    if environ.get(Constants.LOGGING_LEVEL) == Constants.DEBUG:
        level = logging.DEBUG
    
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    return logger
