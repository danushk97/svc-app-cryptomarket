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
        Retrieves list of all available crypto-currency market summaries.

        Returns:
            List[CryptoMarketSummary]: A list of CryptoMarketSummary.
        """
        return self.cryto_market_summaries.list()

    def retrieve_market_summary_for(self, market: str) -> CryptoMarketSummary:
        """
        Retrieves crypto-currency market summary for given market.

        Returns:
            CryptoMarketSummary: A crypt-current market summary.
        """
        return self.cryto_market_summaries.find_by_market(market)
