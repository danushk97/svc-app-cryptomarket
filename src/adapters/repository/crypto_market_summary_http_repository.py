"""
This module provides a repository class for CryptoMarketSummary data management.
"""

from typing import List

from src.adapters.data_source.http_client import HttpClient
from src.config import Config
from src.domain.crypto_market_summary import CryptoMarketSummary
from src.service.interface.abstract_repository import AbstractRepository


class CryptoMarketSummaryHttpRepository(AbstractRepository):
    """
    The `CryptoMarketSummaryHttpRepository` class represents a repository 
    for managing data. It encapsulates the functionality for retrieving, and 
    manipulating data in the repository. It serves as an abstraction layer 
    for interacting with the underlying data source.
    """

    def __init__(self, http_client: HttpClient, base_url: str = None) -> None:
        self.__http_client = http_client
        self.__base_url = base_url or Config.BITTREX_SERVICE_BASE_URL
    
    def list(self) -> List[CryptoMarketSummary]:
        """
        Retrieves and returns a list of all crypto-currency market summaries.

        Returns:
            List[CryptoMarketSummary]: A list of available CryptoMarketSummary.
        """
        response_data = self.__http_client.get(
            self.__base_url,
            Config.ALL_MARKETS_SUMMARY_ENDPOINT
        )

        return [
            CryptoMarketSummary.from_dict(data)
            for data in response_data
        ]

    def find_by_summary(self, summary):
        return super().find_by_summary(summary)
    