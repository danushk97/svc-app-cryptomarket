from src.domain.crypto_market_summary import CryptoMarketSummary


def assert_values(crypto_market_summary: CryptoMarketSummary, args: tuple) -> None:
    assert crypto_market_summary.symbol == args[0]
    assert crypto_market_summary.high == args[1]
    assert crypto_market_summary.low == args[2]
    assert crypto_market_summary.volume == args[3]
    assert crypto_market_summary.quote_volume == args[4]
    assert crypto_market_summary.percent_change == args[5]
    assert crypto_market_summary.updated_at == args[6]


def test_instantiate_crypto_market_summary_class_returns_instance_with_values():
    args = (
        "1ECO-BTC", 
        "0.000010130000", 
        "0.000009550000", 
        "299.05366098", 
        "0.00286879", 
        "6.07", 
        "2023-07-13T04:39:44.69Z"
    )

    crypto_market_summary = CryptoMarketSummary(*args)
    assert_values(crypto_market_summary, args)


def test_from_dict_returns_instance_with_provided_values():
    market_summary_dict = {
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quoteVolume": "0.00286879",
        "percentChange": "6.07",
        "updatedAt": "2023-07-13T04:39:44.69Z"
    }

    crypto_market_summary = CryptoMarketSummary.from_dict(market_summary_dict)
    assert_values(crypto_market_summary, tuple(market_summary_dict.values()))


def test_to_dict_given_instance_returns_dict():
    market_summary_dict = {
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quoteVolume": "0.00286879",
        "percentChange": "6.07",
        "updatedAt": "2023-07-13T04:39:44.69Z"
    }

    crypto_market_summary = CryptoMarketSummary.from_dict(market_summary_dict)
    result = crypto_market_summary.to_dict()
    assert result == market_summary_dict
    