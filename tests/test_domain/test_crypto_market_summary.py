from collections import OrderedDict

from src.domain.crypto_market_summary import CryptoMarketSummary


def assert_values(
    crypto_market_summary: CryptoMarketSummary,
    args: list
) -> None:
    assert crypto_market_summary.symbol == args[0]
    assert crypto_market_summary.high == args[1]
    assert crypto_market_summary.low == args[2]
    assert crypto_market_summary.volume == args[3]
    assert crypto_market_summary.quote_volume == args[4]
    assert crypto_market_summary.percent_change == args[5]
    assert crypto_market_summary.updated_at == args[6]


def test_create_crypto_market_summary_class_returns_instance_with_values():
    args = [
        "1ECO-BTC",
        "0.000010130000",
        "0.000009550000",
        "299.05366098",
        "0.00286879",
        "6.07",
        "2023-07-13T04:39:44.69Z"
    ]

    crypto_market_summary = CryptoMarketSummary(*args)
    assert_values(crypto_market_summary, args)


def test_from_dict_given_valid_dict_returns_instance_with_provided_values(
    camel_case_market_summary_dict
):
    crypto_market_summary = CryptoMarketSummary.from_dict(
        camel_case_market_summary_dict
    )
    assert_values(
        crypto_market_summary,
        list(camel_case_market_summary_dict.values())
    )


def test_from_dict_given_dict_with_missing_values_returns_instance_with_empty_string():  # noqa: E501
    market_summary_dict = OrderedDict({
        "symbol": "1ECO-BTC",
        "high": "0.000010130000",
        "low": "0.000009550000",
        "volume": "299.05366098",
        "quoteVolume": "0.00286879",
        "updatedAt": "2023-07-13T04:39:44.69Z"
    })  # dict without percentChange
    excepted_values = list(market_summary_dict.values())
    excepted_values.insert(5, "")

    crypto_market_summary = CryptoMarketSummary.from_dict(market_summary_dict)
    assert_values(crypto_market_summary, excepted_values)


def test_to_dict_given_instance_returns_dict(
    camel_case_market_summary_dict, snake_case_market_summary_dict
):
    crypto_market_summary = CryptoMarketSummary.from_dict(
        camel_case_market_summary_dict
    )
    result = crypto_market_summary.to_dict()
    assert result == snake_case_market_summary_dict
