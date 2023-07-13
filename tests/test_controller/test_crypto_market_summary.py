import pytest

from tests.fakes.fake_service import FakeCryptoMarketSummaryService


service_path = "src.controller.crypto_market_summary.CryptoMarketSummaryService"


@pytest.fixture()
def fake_service(monkeypatch):
    monkeypatch.setattr(
        service_path, FakeCryptoMarketSummaryService
    )


def test_get_crypto_currency_market_summary_returns_ok_response(
    fake_service, test_client, snake_case_market_summary_dict
):

    response = test_client.get("/crypto/markets/summaries")
    response_json = response.get_json()
    assert response.status_code == 200
    assert len(response_json) == 1
    assert response_json[0] == snake_case_market_summary_dict
