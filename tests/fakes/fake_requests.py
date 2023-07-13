from requests.exceptions import RequestException


class FakeSuccessRequests:
    def get(hostname, resouce_path, params=None, **kwargs):
        return {
            'data': 'mock' 
        }

class FakeFailureRequests(FakeSuccessRequests):
    def get(hostname, resouce_path, params=None, **kwargs):
        raise RequestException('Failed to fetch data')