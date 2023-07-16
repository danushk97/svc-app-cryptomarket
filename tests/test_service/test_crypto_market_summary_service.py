from unittest.mock import create_autospec

import pytest

from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository
from src.service.crypto_market_summary_service import \
    CryptoMarketSummaryService
from src.domain.crypto_market_summary import CryptoMarketSummary


market_summary_dict = {
    "symbol": "1ECO-BTC",
    "high": "0.000010130000",
    "low": "0.000009550000",
    "volume": "299.05366098",
    "quoteVolume": "0.00286879",
    "percentChange": "6.07",
    "updatedAt": "2023-07-13T04:39:44.69Z"
}


@pytest.fixture()
def fake_repository():
    fake_repo = create_autospec(
        CryptoMarketSummaryHttpRepository,
        instance=True
    )
    summary = CryptoMarketSummary.from_dict(market_summary_dict)

    fake_repo.list.return_value = [summary]
    fake_repo.find_by_market.return_value = summary

    yield fake_repo


def test_retrieve_all_market_summaries_returns_list_of_market_summaries(
    fake_repository
):
    service = CryptoMarketSummaryService(fake_repository)
    data = service.retrieve_all()
    assert len(data) == 1
    assert data[0] == CryptoMarketSummary.from_dict(market_summary_dict)


def test_retrieve_market_summary_for_returns_instance(
    fake_repository
):
    service = CryptoMarketSummaryService(fake_repository)
    data = service.retrieve_market_summary_for("test-market")
    assert data == CryptoMarketSummary.from_dict(market_summary_dict)
