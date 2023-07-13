from os import environ

from src.logs import get_logger


def test_get_logger_returns_configured_logger_instance():
    logger = get_logger(__name__)
    assert logger.name == __name__
    assert logger.level == environ["LOGGING_LEVEL"]
