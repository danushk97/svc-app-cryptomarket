"""
This module provides a service class for CryptoMarketSummary data.
"""

from typing import List

from src.domain.crypto_market_summary import CryptoMarketSummary
from src.service.interface.abstract_repository import AbstractRepository


class CryptoMarketSummaryService:
    """
    The class `CryptoMarketSummaryService` that encapsulates the business logic 
    operations and interacts with the repository to fetch and manipulate data.
    """

    def __init__(self, repository: AbstractRepository) -> None:
        self.cryto_market_summaries = repository
    
    def retrieve_all(self) -> List[CryptoMarketSummary]:
        """
        retrieves list of all available crypto-currency market summaries.

        Returns:
            List[CryptoMarketSummary]: A list of CryptoMarketSummary.
        """
        return self.cryto_market_summaries.list()
    