from unittest.mock import patch

from pytest import mark

from src.config import Config


def test_config_init_returns_none_if_all_required_configs_exists():
    assert Config.init() is None
    assert Config.BITTREX_SERVICE_BASE_URL == "http://test-base-url.com"
    assert Config.ALL_MARKETS_SUMMARY_ENDPOINT == "/summaries"
    assert Config.MARKET_SUMMARY_ENDPOINT == "/market/summary"


@mark.parametrize('input', [
    ({}),
    ({'MARKET_SUMMARY_ENDPOINT': '/summary'})
])
def test_config_init_exit_app_on_empty_or_missing_configs(monkeypatch, input):
    monkeypatch.setattr('src.config.dotenv_values', lambda x: {})
    with patch('src.config._exit') as mock_exit:
        assert Config.init() is None
        mock_exit.assert_called_with(1)
