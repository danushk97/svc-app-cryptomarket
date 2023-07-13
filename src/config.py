"""
This module provides configuration settings for the application.
"""

from os import _exit, environ

from dotenv import dotenv_values

from src.constants import Constants


_REQUIRED_CONFIGS = [
    "BITTREX_SERVICE_BASE_URL",
    "ALL_MARKETS_SUMMARY_ENDPOINT",
    "MARKET_SUMMARY_ENDPOINT" 
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
    FLASK_ENV = environ.get(Constants.FLASK_ENV, Constants.DEV)

    @classmethod
    def init(cls) -> None:
        """
        Loads the configs from `{FLASK_ENV}.env` and initialzes the
        class level attributes. 
        """
        missing_configs = []
        config_dict = dotenv_values(f"{cls.FLASK_ENV}.env")
        if not config_dict:
            _exit(1)

        for key, value in config_dict.items():
            if key in _REQUIRED_CONFIGS and value is None:
                missing_configs.append(key)

            setattr(cls, key, value)
        
        if missing_configs:
            _exit(1)
