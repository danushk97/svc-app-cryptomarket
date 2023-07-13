"""
This module provides an abstract base class for repository.
"""

from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    The `AbstractRepository` class defines the common interface and behavior
    for interacting with an repository.
    """
    
    @abstractmethod
    def list(self):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_summary(self, summary):
        raise NotImplementedError
    