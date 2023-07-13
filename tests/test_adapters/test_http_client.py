from tests.fakes.fake_requests import FakeFailureRequests, FakeSuccessRequests
from src.adapters.http_client import HttpClient


def test_http_get_returns_response_data_on_successful_request():
    data = HttpClient(FakeSuccessRequests).get('http://test.com', '/')
    assert data == {
        'data': 'mock'
    }


def test_http_get_raises_app_exception_on_successful_request():
    data = HttpClient(FakeFailureRequests).get('http://test.com', '/')
    assert data == {
        'data': 'mock'
    }
