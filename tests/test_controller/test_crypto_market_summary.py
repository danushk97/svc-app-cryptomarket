def test_get_crypto_currency_market_summary_returns_ok_response(test_client):
    response = test_client.get('/crypto/markets/summaries')

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "UP"
    }
