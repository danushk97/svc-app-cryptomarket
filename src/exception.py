"""
This module provides base exception class for the custom application exception.
"""

from http import HTTPStatus

from src.error_codes import ErrorCode


class AppException(Exception):
    """
    The `AppException` class serves as a base class for custom exceptions
    that can be raised within the application.

    Attributes:
        title (str): A short, human-readable summary of the problem type.
        detail (str): An human readable explanation specific to this occurrence of the problem.
        status (HTTPStatus): The HTTP status code.
        type (str): A URI that identifies the problem type or "about:blank"
    """
    
    def __init__(
        self, 
        title: str = ErrorCode.INTERNAL_SERVER_ERROR.value,
        detail: str = "Unknown error has occured",
        status : HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
        type: str = "about:blank",
        log_message: str = ''
    ) -> None:
        self.title = title
        self.detail = detail
        self.status = status
        self.type = type
        self.__log_message = log_message
    