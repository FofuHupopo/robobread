import os
import requests

from django.db import models
from enum import Enum

from api.security.models import SynchronizerTokenModel


class SynchronizerEndpoints(Enum):
    ORDER = "machine-order"
    CATEGORY = "machine-category"
    PRODUCT = "machine-product"
    CELL = "machine-cell"
    PRODUCT_IN_CELL = "machine-product-in-cell"
    REGISTER_MACHINE = "register-machine"
    EMPTY = ""


class SyncableModel(models.Model):
    is_sync = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def sync(self):
        if self.is_sync:
            return

        if self.is_new:
            status = SynchronizerService().post(self.sync_endpoint(), data=self.to_dict(), is_auth=True)
        else:
            status = SynchronizerService().put(self.sync_endpoint(), data=self.to_dict(), key=self.key())

        if status:
            self.is_new = False
            self.save(is_sync=True)
    
    def remove(self):
        SynchronizerService().delete(self.sync_endpoint(), data=self.to_dict(), key=self.key())

    def save(self, is_sync=False, *args, **kwargs):
        self.is_sync = is_sync

        super().save(*args, **kwargs)

    @staticmethod
    def sync_endpoint() -> SynchronizerEndpoints:
        ...
    
    @staticmethod
    def key() -> str:
        ...

    def to_dict(self) -> dict:
        return dict()


class SynchronizerService:
    def __init__(self):
        self.ip = os.environ.get("SYNCHRONIZER_SERVER_IP")
        self.base_url = f"http://{self.ip}/api/synchronizer"
        self.headers = {}

    def request(self, method: str, endpoint: SynchronizerEndpoints, data: dict=None, is_auth: bool=True, key: str=None) -> requests.Response:
        if is_auth:
            self.headers["Machine-Token"] = get_token()

        url = f"{self.base_url}/{endpoint.value}"

        if key is not None:
            value = data.get(key)

            if value is None:
                raise Exception(f"Key {key} not found in data")

            url = f"{url}/{value}"

        response: requests.Response = getattr(requests, method)(url, json=data, headers=self.headers)
        
        return response
    
    def get(self, endpoint: SynchronizerEndpoints, data: dict=None, is_auth: bool=True, key: str=None) -> bool:
        try:
            response = self.request("get", endpoint, data, is_auth, key)
            return response.status_code < 300
        except requests.ConnectionError:
            return False
    
    def post(self, endpoint: SynchronizerEndpoints, data: dict=None, is_auth: bool=True, key: str=None) -> bool:
        try:
            response = self.request("post", endpoint, data, is_auth, key)
            return response.status_code < 300
        except requests.ConnectionError:
                return False
    
    
    def put(self, endpoint: SynchronizerEndpoints, data: dict=None, is_auth: bool=True, key: str=None) -> bool:
        try:
            response = self.request("put", endpoint, data, is_auth, key)
            return response.status_code < 300
        except requests.ConnectionError:
                return False
    
    def delete(self, endpoint: SynchronizerEndpoints, data: dict=None, is_auth: bool=True, key: str=None) -> bool:
        try:
            response = self.request("delete", endpoint, data, is_auth, key)
            return response.status_code < 300
        except requests.ConnectionError:
                return False


def fetch_and_save_token() -> str:
    response = SynchronizerService().request(
        method="post",
        endpoint=SynchronizerEndpoints.REGISTER_MACHINE,
        data={
            "sku": os.environ.get("VENDING_MACHINE_SKU"),
            "name": os.environ.get("VENDING_MACHINE_NAME"),
            "address": os.environ.get("VENDING_MACHINE_ADDRESS"),
        },
        is_auth=False
    )

    try:
        token = response.json()["token"]
        SynchronizerTokenModel.objects.update_or_create(id=1, defaults={"token": token})
        return token
    except KeyError:
        raise Exception("Token not found")


def get_token() -> str:
    try:
        api_token = SynchronizerTokenModel.objects.get(id=1)
        return str(api_token.token)
    except SynchronizerTokenModel.DoesNotExist:
        return fetch_and_save_token()
