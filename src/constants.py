"""
This module is responsible for holding constants that are used
application wide.
"""


class Constants:
    """
    The `Constants` holds the string constants that are used application wide.
    """

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

    # Flask env"s
    ENV = "ENV"
    TEST = "test"
    DEV = "dev"
    STAGE = "stage"
    PROD = "prod"

    LOGGING_LEVEL = "LOGGING_LEVEL"
    RESPONSE = "response"

    # Logging levels
    DEBUG = "DEBUG"
    INFO = "INFO"

    # BITTREX API request headers.
    API_KEY = "api-key"
    API_TIMESTAMP = "api-timestamp"
    API_SIGNATURE = "api-signature"
    API_CONTENT_HASH = "api-content-hash"

    @staticmethod
    def snake_to_camel_case(value: str) -> str:
        """
        Converts a string value to camelCase string values if the provided
        value is in snake_case, if not returns the same value.

        Args:
            value (string): Any string value. Ex: user_id

        Returns:
            str: CamelCased string value.
        """
        first_value, *value_parts = value.split("_")

        return first_value + "".join(value.title() for value in value_parts)


class HTTPStatus:
    INTERNAL_SERVER_ERROR = 500
    NOT_FOUND = 404
    OK = 200
