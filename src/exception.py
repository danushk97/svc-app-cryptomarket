"""
This module provides base exception class for the custom application exception.
"""

from dataclasses import dataclass, field, asdict
from http import HTTPStatus

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
        status (HTTPStatus): The HTTP status code.
        type (str): A URI that identifies the problem type or "about:blank"
    """ 

    title: str = ErrorCode.INTERNAL_SERVER_ERROR.value
    detail: str = (
        "The server encountered an internal error and was unable to complete "
        "your request"
    )
    status : HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR.value
    type: str = "about:blank"
    _log_message: str = field(default="", repr=False)
    
    def to_dict(self) -> dict:
        data = asdict(self)
        data.pop("_log_message")

        return data
    
    def __str__(self) -> str:
        return repr(self)
    