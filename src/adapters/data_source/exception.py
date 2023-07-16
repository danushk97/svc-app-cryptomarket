"""
This module provides a custom exception class for external service failure.
"""

from dataclasses import dataclass

from src.exception import AppException
from src.error_codes import ErrorCode


@dataclass
class ExternalServiceException(AppException):
    """
    The class `ExternalServiceException` is raised when the application
    encounters an error on external service call.
    """


@dataclass
class ResourceNotFoundException(ExternalServiceException):
    status: int = 404
    title: str = ErrorCode.NOT_FOUND
    detail: str = (
        "The requested URL was not found on the server. If you entered the URL"
        " manually please check your spelling and try again."
    )
