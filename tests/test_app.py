from flask import Flask

from src.app import create_app


def test_create_app_returns_instance_of_flask_app():
    app = create_app()
    assert isinstance(app, Flask)
    