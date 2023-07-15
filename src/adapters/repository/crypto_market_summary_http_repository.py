"""
This module provides a repository class for CryptoMarketSummary data management.
"""

import time
import json
from typing import List
from urllib.parse import urljoin

from src.adapters.data_source.http_client import HttpClient
from src.adapters.repository import utils
from src.config import Config
from src.constants import Constants
from src.domain.crypto_market_summary import CryptoMarketSummary
from src.service.interface.abstract_repository import AbstractRepository


class CryptoMarketSummaryHttpRepository(AbstractRepository):
    """
    The `CryptoMarketSummaryHttpRepository` class represents a repository 
    for managing data. It encapsulates the functionality for retrieving, and 
    manipulating data in the repository. It serves as an abstraction layer 
    for interacting with the underlying data source.
    """

    def __init__(
        self, 
        http_client: HttpClient = None, 
        base_url: str = None
    ) -> None:
        self.__http_client = http_client or HttpClient()
        self.__base_url = base_url or Config.BITTREX_SERVICE_BASE_URL
    
    def list(self) -> List[CryptoMarketSummary]:
        """
        Retrieves and returns a list of all crypto-currency market summaries.

        Returns:
            List[CryptoMarketSummary]: A list of available CryptoMarketSummary.
        """
        data = self.__make_http_request(Config.ALL_MARKETS_SUMMARY_ENDPOINT)

        return [
            CryptoMarketSummary.from_dict(data)
            for data in data
        ]

    def find_by_market(self, market: str) -> CryptoMarketSummary:
        """
        Retrieves crypto-currency market summaries for the given market.

        Args:
            market (str): A string denoting a market.

        Returns:
            CryptoMarketSummary: A crypto-currency market summary.
        """
        data = self.__make_http_request(
            Config.MARKET_SUMMARY_ENDPOINT.format(market=market)
        )

        return CryptoMarketSummary.from_dict(data)

    def __make_http_request(
        self, 
        resource_path, 
        http_method: str = Constants.GET
    ):
        url = urljoin(self.__base_url, resource_path)
        headers = self.__generate_request_headers(http_method, url)
        response_data = getattr(self.__http_client, http_method)(
            url,
            headers=headers
        )

        return response_data
    
    def __generate_request_headers(self, 
        http_method: str,
        url: str,
        request_body = ""
    ):
        if request_body and isinstance(request_body, dict):
            request_body = json.dumps(request_body)

        content_hash = utils.calculate_sha512_hash(request_body)
        timestamp = int(time.time()) * 1000
        headers = {
            Constants.API_KEY: Config.BITTREX_API_KEY,
            Constants.API_TIMESTAMP: timestamp,
            Constants.API_CONTENT_HASH: content_hash
        }
        pre_sign = "".join([
            str(timestamp), 
            url,
            http_method.upper(), 
            content_hash, 
            ""
        ])
        headers.update(
            {
                Constants.API_SIGNATURE: utils.calculate_hmac_sha512_signature(
                    pre_sign, Config.BITTREX_SECRET_KEY
                )
            }
        )
        
        return headers
    