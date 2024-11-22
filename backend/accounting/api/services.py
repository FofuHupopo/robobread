import requests

from typing import Mapping
from dataclasses import dataclass
from json.decoder import JSONDecodeError

from .exceptions import ServiceResponseException


@dataclass
class BaseData:
    ...


class BaseService:
    def __init__(self, base_url: str) -> None:
        self.URLS = dict()
        self.BASE_URL = base_url

    def active_sync(self) -> BaseData:
        ...

    def inactive_sync(self) -> BaseData:
        ...
    
    def sync(self) -> BaseData:
        if self.is_active():
            data_object = self.active_sync()
        else:
            data_object = self.inactive_sync()

        return data_object

    def is_active(self) -> bool:
        return True

    def update_urls(self, urls: Mapping[str, str]) -> None:
        self.URLS.update(urls)

    def _request(self, method, url: str, sub_url: str, data: dict={}, files: dict={}) -> requests.Response:
        r: requests.Response = method(
            f"{url}/{sub_url}",
            data=data,
            files=files
        )

        try:
            response = r.json()
        except JSONDecodeError:
            response = r.text

        if r.status_code >= 400:
            raise ServiceResponseException(
                "Service response error",
                response=response,
                status_code=r.status_code
            )

        return response
    
    def get_request(self, sub_url: str) -> requests.Response:
        r = self._request(
            method=requests.get,
            url=self.BASE_URL,
            sub_url=sub_url,
        )

        return r
    
    def post_request(self, sub_url: str, data: dict, files: dict = {}) -> requests.Response:
        r = self._request(
            method=requests.post,
            url=self.BASE_URL,
            sub_url=sub_url,
            data=data,
            files=files
        )

        return r
    
    def put_request(self, sub_url: str, data: dict, files: dict = {}) -> requests.Response:
        r = self._request(
            method=requests.put,
            url=self.BASE_URL,
            sub_url=sub_url,
            data=data,
            files=files
        )

        return r
    
    def delete_request(self, sub_url: str) -> requests.Response:
        r = self._request(
            method=requests.delete,
            url=self.BASE_URL,
            sub_url=sub_url
        )

        return r
