from unittest.mock import create_autospec

from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository
from src.adapters.data_source.http_client import HttpClient


def test_get_retrieve_crypto_market_summary_returns_list_of_market_summary():
    market_summary_dict = {
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quoteVolume": "0.00286879",
        "percentChange": "6.07",
        "updatedAt": "2023-07-13T04:39:44.69Z"
    }
    mock_http_client = create_autospec(HttpClient, instance=True)
    mock_http_client.get.return_value = [market_summary_dict]

    crypto_market_summary_list = CryptoMarketSummaryHttpRepository(
        mock_http_client
    ).list()
    assert len(crypto_market_summary_list) == 1
    crypto_market_summary_list[0] == market_summary_dict
