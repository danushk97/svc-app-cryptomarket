import logging

from src.logs import get_logger


def test_get_logger_returns_configured_logger_instance():
    logger = get_logger(__name__)
    assert isinstance(logger, logging.Logger)
    assert logger.name == __name__
    assert logger.level == 10  # Logging Level for DEBUG
