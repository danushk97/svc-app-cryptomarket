from src.domain.crypto_market_summary import CryptoMarketSummary


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
    crypto_market_sumary = CryptoMarketSummary(*args)
    assert crypto_market_sumary.symbol == args[0]
    assert crypto_market_sumary.high == args[1]
    assert crypto_market_sumary.low == args[2]
    assert crypto_market_sumary.volume == args[3]
    assert crypto_market_sumary.quote_volume == args[4]
    assert crypto_market_sumary.percent_change == args[5]
    assert crypto_market_sumary.updated_at == args[6]
