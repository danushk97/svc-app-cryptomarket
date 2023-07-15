"""
This module provides an HTTP client for making HTTP requests.
"""

from urllib.parse import urljoin
from http import HTTPStatus

import requests

from src.constants import Constants
from src.adapters.data_source.exception import ExternalServiceException, \
    ResourceNotFoundException
from src.logs import get_logger


_logger = get_logger(__name__)


class HttpClient:
    """
    The `HttpClient` class encapsulates the functionality for sending HTTP 
    requests and handling responses. It provides a convenient interface for 
    interacting with HTTP-based APIs.
    """

    def __init__(self, proxy=requests) -> None:
        self.__proxy = proxy

    def __make_request(
        self,
        http_method: str, 
        url: str,
        params: dict = None,
        data: dict = None,
        **kwargs
    ) -> dict:
        """
        Performs a HTTP request and returns response.

        Args:
            url (str): The target URL.
            params (dict, optional): Optional query string/param if any.
            data (dict, optional): Optional request body.
            kwargs (dict, optional): Additional request detail, Ex: headers
        
        Returns:
            dict: Resposne JSON.
        
        Raises:
            AppException: If requests.RequestException is raised.
        """
        method = getattr(self.__proxy, http_method)
        params = params or {}
        data = data or {}
        
        failed_log_message = f"[UNSUCCESSFUL EXTERNAL SERVICE CALL]: "

        _logger.info(f"[STARTING EXTERNAL SERVICE CALL]: {url}")

        try:
            response = method(url, params=params, data=data, **kwargs)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            _logger.error(
                failed_log_message + f"{http_err}. {http_err.response.text}"
            )
            if http_err.response.status_code == HTTPStatus.NOT_FOUND:
                raise ResourceNotFoundException() from http_err 

            raise ExternalServiceException() from http_err
        except requests.RequestException as req_err:
            _logger.error(failed_log_message + f"{req_err}")

            raise ExternalServiceException() from req_err
        
        _logger.info(
            f"[SUCCESSFUL EXTERNAL SERVICE CALL]: {response.status_code} {url}"
        )

        return response.json()

    def get(
        self, 
        base_url: str, 
        resource_path: str, 
        params: dict = None, 
        **kwargs
    ) -> dict:
        """
        Retrieves data using HTTP get.

        Args:
            base_url (str): The base URL.
            resource_path (str): The URL path.
            params (dict, optional): Query string/param if any.
            kwargs (dict, optional): Additional request detail, Ex: headers
        
        Returns:
            dict: Response json.
        """
        return self.__make_request(
            Constants.GET,
            urljoin(base_url, resource_path),
            params,
            **kwargs 
        )
    