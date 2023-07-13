"""
This module provides an abstract base class for repository.
"""

from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    The `AbstractRepository` class defines the common interface and behavior
    for interacting with an repository.

    Attributes:
        data_source: Any class or instance that is responsible to fetch data.
    """

    def __init__(self, data_source: str) -> None:
        self.data_source = data_source
    
    @abstractmethod
    def list(self):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_summary(self, summary):
        raise NotImplementedError
    