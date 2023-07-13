from requests.exceptions import RequestException


class FakeResponse:
    @staticmethod
    def json():
        return {
            'data': 'mock'
        }


class FakeSuccessRequests:
    def get(url, params=None, **kwargs):
        return FakeResponse


class FakeFailureRequests(FakeSuccessRequests):
    def get(hostname, resouce_path, params=None, **kwargs):
        raise RequestException('Failed to fetch data')
    