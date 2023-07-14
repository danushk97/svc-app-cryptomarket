"""
This module provides the function that is responsible to create, configure
and initialize FLASK APP.
"""

import os

import connexion

from src import error_handlers
from src.exception import AppException
from src.config import Config


def create_app():
    """
    Creates and configures flask app using connexion.
    """
    Config.init()
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    connex_app = connexion.App(__name__, specification_dir=basedir)
    connex_app.add_api("swagger.yml", strict_validation=True)

    connex_app.app.register_error_handler(
        AppException, 
        error_handlers.app_error_handler
    )
    connex_app.app.register_error_handler(
        Exception, 
        error_handlers.generic_error_handler
    )
    
    return connex_app.app
