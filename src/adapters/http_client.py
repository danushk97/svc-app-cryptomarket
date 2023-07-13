from dataclasses import dataclass
from urllib.parse import urljoin

import requests

from src.constants import Constants


class HttpClient:
    def __init__(self, proxy=requests) -> None:
        self.__proxy = proxy

    def __make_request(
        self,
        http_method: str, 
        url: str,
        params: dict = None,
        data: dict = None,
        **kwargs
    ):
        method = getattr(self.__proxy, http_method)
        params = params or {}
        data = data or {}
        try:
            response = method(url, params=params, data=data, **kwargs)
        except requests.exceptions.RequestException as err:
            raise Exception from err
        
        return response.json()

    def get(self, base_url, resource_path, params=None, **kwargs):
        return self.__make_request(
            Constants.GET,
            urljoin(base_url, resource_path),
            params,
            **kwargs 
        )
    