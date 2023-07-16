import pytest

from tests.fakes.fake_hashlib import FakeHashlib
from src.adapters.repository import utils


@pytest.fixture(autouse=True)
def fake_hashinglib(monkeypatch):
    monkeypatch.setattr("src.adapters.repository.utils.hashlib", FakeHashlib())
    monkeypatch.setattr("src.adapters.repository.utils.hmac", FakeHashlib())


def test_calculate_sha512_hash():
    assert utils.calculate_sha512_hash("value") == b"value"


def test_calculate_hmac_sha512_signature():
    assert utils.calculate_hmac_sha512_signature("secret", "value") == b"value"
