"""
This module provides all the app initializer functions.
"""

import time

from flask import g, request, Flask

from src import error_handlers
from src.config import Config
from src.exception import AppException
from src.logs import get_logger


_logger = get_logger(__name__)


def _log_request_start():
    _logger.info(f"STARTED processing {request.url}")
    _logger.debug(f"Request Headers: {request.headers}")

    g.start_time = time.time()


def _log_request_end(exception=None):
    elapsed_time = time.time() - g.get("start_time")
    _logger.info(
        f"FINISHED processing {request.url} in {elapsed_time:.6f} seconds"
    )


def init_app(app: Flask):
    _logger.info("Loading app configs...")
    Config.init()  # Loads and initializes the app configs.

    _logger.info("Registering error handlers...")
    app.register_error_handler(AppException, error_handlers.app_error_handler)
    app.register_error_handler(Exception, error_handlers.generic_error_handler)
    
    _logger.info("Registering before_request and teardown_request...")
    app.before_request(_log_request_start)
    app.teardown_request(_log_request_end)
    