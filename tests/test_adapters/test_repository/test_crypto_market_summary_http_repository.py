
import pytest

from tests.fakes.fake_http_client import FakeHttpClient
from tests.fakes.fake_utils import FakeUtils
from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository
from src.domain.crypto_market_summary import CryptoMarketSummary
from src.adapters.data_source.exception import ResourceNotFoundException


@pytest.fixture(autouse=True)
def fake_utils_and_time(monkeypatch):
    monkeypatch.setattr(
        "src.adapters.repository.crypto_market_summary_http_repository.utils",
        FakeUtils()
    )
    monkeypatch.setattr(
        (
            "src.adapters.repository.crypto_market_summary_http_repository."
            "time.time"
        ),
        lambda: 200
    )


@pytest.fixture()
def expected_headers():
    return {
        "api-content-hash": "sha512_hash_value",
        "api-key": "test-key",
        "api-signature": "test-secret:200000{url}GETsha512_hash_value",
        "api-timestamp": "200000"
    }


def test_get_retrieve_crypto_market_summary_returns_list_of_market_summary(
    snake_case_market_summary_dict, expected_headers
):
    fake_http_client = FakeHttpClient([snake_case_market_summary_dict])
    expected_headers["api-signature"] = \
        expected_headers["api-signature"].format(
        url="http://test-base-url.com/all-summaries"
    )

    crypto_market_summary_list = CryptoMarketSummaryHttpRepository(
        fake_http_client
    ).list()
    assert fake_http_client.headers == expected_headers
    assert len(crypto_market_summary_list) == 1
    assert crypto_market_summary_list[0] == CryptoMarketSummary.from_dict(
        snake_case_market_summary_dict
    )


def test_get_find_by_market_given_valid_input_then_returns_data(
    snake_case_market_summary_dict, expected_headers
):
    fake_http_client = FakeHttpClient(snake_case_market_summary_dict)
    expected_headers["api-signature"] = \
        expected_headers["api-signature"].format(
        url="http://test-base-url.com/summary"
    )

    crypto_market_summary = CryptoMarketSummaryHttpRepository(
        fake_http_client
    ).find_by_market(
        "test-summary"
    )
    assert crypto_market_summary == CryptoMarketSummary.from_dict(
        snake_case_market_summary_dict
    )
    assert fake_http_client.headers == expected_headers


def test_get_find_by_market_given_invalid_summary_then_raises_external_serivce_exception(  # noqa: E501
    snake_case_market_summary_dict
):
    with pytest.raises(ResourceNotFoundException):
        CryptoMarketSummaryHttpRepository(
            FakeHttpClient(snake_case_market_summary_dict, 404)
        ).find_by_market(
            "invalid-summary"
        )
