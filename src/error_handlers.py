from src.exception import AppException
from src.logs import get_logger


_logger = get_logger(__name__)


def app_error_handler(exception: AppException):
    _logger.error(exception, exc_info=True)

    return exception.to_dict(), exception.status


def generic_error_handler(exception: Exception):
    _logger.error(exception, exc_info=True)

    app_exception = AppException()

    return app_exception.to_dict(), app_exception.status
