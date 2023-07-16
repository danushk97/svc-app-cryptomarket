def test_health_check_returns_ok_response(test_client):
    response = test_client.get("/v3/health-check")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "UP"
    }
