import pytest

from tests.fakes.fake_requests import FakeFailureRequests, FakeSuccessRequests,\
    FakeFailureRequestsWithHttpError
from src.adapters.data_source.http_client import HttpClient
from src.exception import AppException


def test_http_get_returns_response_data_on_successful_request():
    data = HttpClient(FakeSuccessRequests).get('http://test.com', '/')
    assert data == {
        'data': 'mock'
    }


def test_http_get_raises_app_exception_on_unexpected_error():
    with pytest.raises(AppException) as exc:
        HttpClient(FakeFailureRequests).get('http://test.com', '/')

    assert exc._excinfo[1].status == 500


def test_http_get_raises_app_exception_on_unsuccessful_request(caplog):
    with pytest.raises(AppException) as exc:
        HttpClient(FakeFailureRequestsWithHttpError).get('http://test.com', '/')

    exc = exc._excinfo[1]
    logs = [record.getMessage() for record in caplog.records]
    expected_log_message = \
        "[UNSUCCESSFUL EXTERNAL SERVICE CALL]: Error. {\"data\": \"mock\"}"
    
    assert exc.status == 500
    assert expected_log_message in logs
