from http import HTTPStatus


def test_health_check_returns_ok_response(test_client):
    response = test_client.get('/health-check')

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {
        "status": "UP"
    }
