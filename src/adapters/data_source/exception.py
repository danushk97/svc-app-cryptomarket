"""
This module provides a custom exception class for external service failure.
"""

from dataclasses import dataclass, field

from src.exception import AppException


@dataclass
class ExternalServiceException(AppException):
    """
    The class `ExternalServiceException` is raised when the application 
    encounters an error on external service call.
    """
    
    _log_message: str = field(
        default="Error occured while communicating with external service.",
        repr=False
    )
