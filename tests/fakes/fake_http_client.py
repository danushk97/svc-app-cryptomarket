from tests.fakes.fake_requests import FakeResponse
from src.adapters.data_source.exception import ResourceNotFoundException


class FakeHttpClient:
    def __init__(self, data, status_code=200)-> None:
        self.data = data
        self.status_code = status_code
    
    def send_request(self, *args, **kwargs):
        if self.status_code == 404:
            raise ResourceNotFoundException()
        
        return self.data
    