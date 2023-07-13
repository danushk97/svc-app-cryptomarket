import pytest

from src.app import create_app


@pytest.fixture(scope="session")
def test_client():
    app = create_app()
    yield app.test_client()
