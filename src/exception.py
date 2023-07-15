"""
This module provides base exception class for the custom application exception.
"""

from dataclasses import dataclass, asdict

from src.constants import HTTPStatus
from src.error_codes import ErrorCode


@dataclass
class AppException(Exception):
    """
    The `AppException` class serves as a base class for custom exceptions
    that can be raised within the application.

    Attributes:
        title (str): A short, human-readable summary of the problem type.
        detail (str): An human readable explanation specific to this 
                      occurrence of the problem.
        status (int): The HTTP status code.
        type (str): A URI that identifies the problem type or "about:blank"
    """ 

    title: str = ErrorCode.INTERNAL_SERVER_ERROR
    detail: str = (
        "The server encountered an internal error and was unable to complete "
        "your request"
    )
    status : int = HTTPStatus.INTERNAL_SERVER_ERROR
    type: str = "about:blank"
    
    def to_dict(self) -> dict:
        data = asdict(self)

        return data
    
    def __str__(self) -> str:
        return repr(self)
    