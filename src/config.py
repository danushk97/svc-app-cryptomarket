"""
This module provides configuration settings for the application.
"""

from os import _exit, environ

from dotenv import dotenv_values

from src.constants import Constants
from src.logs import get_logger


_logger = get_logger(__name__)


_REQUIRED_CONFIGS = [
    "BITTREX_SERVICE_BASE_URL",
    "ALL_MARKETS_SUMMARY_ENDPOINT",
    "MARKET_SUMMARY_ENDPOINT",
    "BITTREX_API_KEY",
    "BITTREX_SECRET_KEY"
]


class Config:
    """
    The `Config` class defines the configuration options and settings
    used by the application. It provides a convenient way to access
    and manage the application's configuration.
    """

    #  External service URL details.
    BITTREX_SERVICE_BASE_URL = None
    ALL_MARKETS_SUMMARY_ENDPOINT = None
    MARKET_SUMMARY_ENDPOINT = None

    ENV = environ.get(Constants.ENV, Constants.DEV)

    # Bittrex API secrets.
    BITTREX_API_KEY = None
    BITTREX_SECRET_KEY = None

    @classmethod
    def init(cls) -> None:
        """
        Loads the configs from `{ENV}.env` and initialzes the
        class level attributes.
        """
        missing_configs = []
        config_dict = dotenv_values(f"{cls.ENV}.env")

        if not config_dict:
            _logger.critical(
                "Aborting application start up due to empty configs."
            )

            _exit(1)

        for key in _REQUIRED_CONFIGS:
            if key not in config_dict:
                missing_configs.append(key)
                continue

            setattr(cls, key, config_dict[key])

        if missing_configs:
            _logger.critical(
                "Aborting application start up due to missing "
                f"configs {missing_configs}."
            )

            _exit(1)
