import pytest

from tests.fakes.fake_requests import FakeFailureRequests, FakeSuccessRequests
from src.adapters.http_client import HttpClient
from src.exception import AppException


def test_http_get_returns_response_data_on_successful_request():
    data = HttpClient(FakeSuccessRequests).get('http://test.com', '/')
    assert data == {
        'data': 'mock'
    }


def test_http_get_raises_app_exception_on_successful_request():
    with pytest.raises(AppException) as exc:
        HttpClient(FakeFailureRequests).get('http://test.com', '/')

    assert exc._excinfo[1].status == 500
    