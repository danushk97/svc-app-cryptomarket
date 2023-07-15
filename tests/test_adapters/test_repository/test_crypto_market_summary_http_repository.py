from unittest.mock import create_autospec

import pytest

from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository
from src.adapters.data_source.http_client import HttpClient
from src.domain.crypto_market_summary import CryptoMarketSummary
from src.adapters.data_source.exception import ExternalServiceException


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

def test_get_find_by_market_given_valid_input_then_returns_data(
    snake_case_market_summary_dict
):
    mock_http_client = create_autospec(HttpClient, instance=True)
    mock_http_client.get.return_value = [snake_case_market_summary_dict]

    crypto_market_summary = CryptoMarketSummaryHttpRepository(
        mock_http_client
    ).find_by_market(
        "test-summary"
    )
    assert crypto_market_summary == CryptoMarketSummary.from_dict(
        snake_case_market_summary_dict
    )


def test_get_find_by_market_given_invalid_summary_then_raises_external_serivce_exception(
    snake_case_market_summary_dict
):
    mock_http_client = create_autospec(HttpClient, instance=True)
    mock_http_client.get.return_value = [snake_case_market_summary_dict]

    with pytest.raises(ExternalServiceException) as exc:
        CryptoMarketSummaryHttpRepository(mock_http_client).find_by_market(
            "invalid-summary"
        )
