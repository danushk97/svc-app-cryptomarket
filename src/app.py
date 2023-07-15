"""
This module provides the function that is responsible to create, configure
and initialize FLASK APP.
"""

import os

import connexion

from src.bootstrap import init_app
from src.logs import get_logger


_logger = get_logger(__name__)


def create_app():
    """
    Creates and configures flask app using connexion.
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    connex_app = connexion.App(__name__, specification_dir=basedir)
    init_app(connex_app.app)
    
    _logger.info("Registering routes...")
    connex_app.add_api(
        "swagger.yml", 
        strict_validation=True,
        base_path="/v3"
    )
    
    return connex_app.app
