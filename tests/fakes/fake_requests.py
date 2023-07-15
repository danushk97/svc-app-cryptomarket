import json

from requests.exceptions import RequestException, HTTPError


class FakeResponse:
    def __init__(self, status_code=200) -> None:
        self.status_code = status_code
        self.text = json.dumps(self.json())

    def json(self):
        return {
            'data': 'mock'
        }

    def raise_for_status(self):
        if self.status_code == 200:
            return 
        
        raise HTTPError('Error', response=self)


class FakeSuccessRequests:
    def get(self, url, params=None, **kwargs):
        return FakeResponse()


class FakeFailureRequests(FakeSuccessRequests):
    def get(self, url, params=None, **kwargs):
        raise RequestException('Unexpected error')


class FakeFailureRequestsWithHttpError(FakeSuccessRequests):
    def __init__(self, status_code=400) -> None:
        self.status_code = status_code

    def get(self, url, params=None, **kwargs):
        return FakeResponse(self.status_code)
    