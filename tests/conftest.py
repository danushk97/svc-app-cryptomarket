from collections import OrderedDict

import pytest

from src.app import create_app
from src.domain.crypto_market_summary import CryptoMarketSummary


@pytest.fixture(scope="session")
def test_client():
    app = create_app()
    yield app.test_client()


def make_crypto_market_summary():
    market_dict = {
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quoteVolume": "0.00286879",
        "percentChange": "6.07",
        "updatedAt": "2023-07-13T04:39:44.69Z"
    }
    return CryptoMarketSummary.from_dict(market_dict)


@pytest.fixture(scope="session")
def crypto_market_summary_instace():
    return make_crypto_market_summary()


@pytest.fixture(scope="session")
def snake_case_market_summary_dict():
    return OrderedDict({
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quote_volume": "0.00286879",
        "percent_change": "6.07",
        "updated_at": "2023-07-13T04:39:44.69Z"
    })


@pytest.fixture(scope="session")
def camel_case_market_summary_dict():
    return OrderedDict({
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quoteVolume": "0.00286879",
        "percentChange": "6.07",
        "updatedAt": "2023-07-13T04:39:44.69Z"
    })
