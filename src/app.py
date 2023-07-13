import os

import connexion


def create_app():
    """
    Creates and configures flask app using connexion.
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    connex_app = connexion.App(__name__, specification_dir=basedir)
    connex_app.add_api("swagger.yml", strict_validation=True)
    
    return connex_app.app
