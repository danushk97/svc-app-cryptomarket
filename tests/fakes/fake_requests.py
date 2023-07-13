from requests.exceptions import RequestException


class FakeResponse:
    def __init__(self, status_code=200) -> None:
        self.status_code = status_code

    def json(self):
        return {
            'data': 'mock'
        }

    def raise_for_status(self):
        return


class FakeSuccessRequests:
    def get(url, params=None, **kwargs):
        return FakeResponse()


class FakeFailureRequests(FakeSuccessRequests):
    def get(url, params=None, **kwargs):
        raise RequestException('Failed to fetch data')
    