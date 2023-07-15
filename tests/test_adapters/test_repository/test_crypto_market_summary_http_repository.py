
import pytest

from tests.fakes.fake_http_client import FakeHttpClient
from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository
from src.domain.crypto_market_summary import CryptoMarketSummary
from src.adapters.data_source.exception import ResourceNotFoundException


def test_get_retrieve_crypto_market_summary_returns_list_of_market_summary(
    snake_case_market_summary_dict
):
    crypto_market_summary_list = CryptoMarketSummaryHttpRepository(
        FakeHttpClient([snake_case_market_summary_dict])
    ).list()
    assert len(crypto_market_summary_list) == 1
    assert crypto_market_summary_list[0] == CryptoMarketSummary.from_dict(
        snake_case_market_summary_dict
    )

def test_get_find_by_market_given_valid_input_then_returns_data(
    snake_case_market_summary_dict
):
    crypto_market_summary = CryptoMarketSummaryHttpRepository(
        FakeHttpClient(snake_case_market_summary_dict)
    ).find_by_market(
        "test-summary"
    )
    assert crypto_market_summary == CryptoMarketSummary.from_dict(
        snake_case_market_summary_dict
    )


def test_get_find_by_market_given_invalid_summary_then_raises_external_serivce_exception(
    snake_case_market_summary_dict
):
    with pytest.raises(ResourceNotFoundException):
        CryptoMarketSummaryHttpRepository(
            FakeHttpClient(snake_case_market_summary_dict, 404)
        ).find_by_market(
            "invalid-summary"
        )
