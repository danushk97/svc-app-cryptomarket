import pytest

from tests.fakes.fake_service import FakeCryptoMarketSummaryService, \
    FakeCryptoMarketSummaryRaisesExceptionService


service_path = "src.controller.crypto_market_summary.CryptoMarketSummaryService"


@pytest.fixture()
def fake_service(monkeypatch):
    monkeypatch.setattr(
        service_path, FakeCryptoMarketSummaryService
    )


@pytest.fixture()
def fake_service_raises_exception(monkeypatch):
    monkeypatch.setattr(
        service_path, FakeCryptoMarketSummaryRaisesExceptionService
    )


def test_get_crypto_currency_market_summary_returns_ok_response(
    fake_service, test_client, snake_case_market_summary_dict
):

    response = test_client.get("/v3/crypto/markets/summaries")
    response_json = response.get_json()
    assert response.status_code == 200
    assert len(response_json) == 1
    assert response_json[0] == snake_case_market_summary_dict


def test_get_crypto_currency_market_summary_returns_not_ok_response_on_error_from_service(
    fake_service_raises_exception, test_client, snake_case_market_summary_dict
):

    response = test_client.get("/v3/crypto/markets/summaries")
    response_json = response.get_json()
    assert response.status_code == 500
    assert response_json == {
        "detail": (
            "The server encountered an internal error and was unable to "
            "complete your request"
        ),
        "status": 500,
        "title": "Internal Server Error",
        "type": "about:blank"
    }


def test_get_crypto_currency_market_summary_returns_ok_response(
    fake_service, test_client, snake_case_market_summary_dict
):

    response = test_client.get("/v3/crypto/markets/test-market/summaries")
    response_json = response.get_json()
    assert response.status_code == 200
    assert response_json == snake_case_market_summary_dict