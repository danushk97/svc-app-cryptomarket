from unittest.mock import create_autospec

from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository
from src.adapters.data_source.http_client import HttpClient
from src.domain.crypto_market_summary import CryptoMarketSummary


def test_get_retrieve_crypto_market_summary_returns_list_of_market_summary(
    snake_case_market_summary_dict
):
    mock_http_client = create_autospec(HttpClient, instance=True)
    mock_http_client.get.return_value = [snake_case_market_summary_dict]

    crypto_market_summary_list = CryptoMarketSummaryHttpRepository(
        mock_http_client
    ).list()
    assert len(crypto_market_summary_list) == 1
    assert crypto_market_summary_list[0] == CryptoMarketSummary.from_dict(
        snake_case_market_summary_dict
    )
