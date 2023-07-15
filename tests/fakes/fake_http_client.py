from requests.exceptions import HTTPError

from tests.fakes.fake_requests import FakeResponse


class FakeHttpClient:
    def __init__(self, data, status_code=200)-> None:
        self.data = data
        self.status_code = status_code
    
    def get(self, *args):
        if self.status_code == 404:
            raise HTTPError("Not Found", response=FakeResponse(400))
        
        return self.data, self.status_code
    