from src.config import Config


def test_config_init_returns_none_if_all_required_configs_exists():
    assert Config.init() is None
    assert Config.BITTREX_SERVICE_BASE_URL == "http://test-base-url.com"
    assert Config.ALL_MARKETS_SUMMARY_ENDPOINT == "/summaries"
    assert Config.MARKET_SUMMARY_ENDPOINT == "/market/summary"