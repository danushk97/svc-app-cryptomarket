"""
This module is responsible for holding constants that are used application wide.
"""

from typing import Any


class Constants:

    # CryptoMarketSummary domain attributes
    SYMBOL = "symbol"
    HIGH = "high"
    LOW = "low"
    VOLUME = "volume"
    QUOTE_VOLUME = "quote_volume"
    UPDATED_AT = "updated_at"
    PERCENT_CHANGE = "percent_change"

    # HTTP method
    GET = "get"

    # Flask env's
    FLASK_ENV = 'FLASK_ENV'
    TEST = 'test'
    DEV = 'dev'
    STAGE = 'stage'
    PROD = 'prod'

    @staticmethod
    def snake_to_camel_case(value: str) -> str:
        first_value_part, *value_parts = value.split("_")

        return first_value_part + ''.join(value.title() for value in value_parts)
