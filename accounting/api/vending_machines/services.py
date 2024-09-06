from __future__ import annotations

import requests

from django.conf import settings
from typing import List, Mapping

from api.services import BaseService
from .data import VendingMachineData
from . import models


PROTOCOL = getattr(settings, "VENDING_MACHINES_PROTOCOL")

URLS = {
    "info": "security/info",
}


class VendingMachineService(BaseService):
    def __init__(self, vending_machine: models.VendingMachineModel) -> None:
        super().__init__()

        self.vending_machine = vending_machine
        self.VENDING_MACHINE_URL = f"{PROTOCOL}://{vending_machine.ip_address}/api"
        self.update_urls(URLS)

    def active_sync(self) -> VendingMachineData:
        self.vending_machine.status = "active"
        self.vending_machine.save()

        return VendingMachineData(
            vending_machine=self.vending_machine, is_active=True
        )

    def inactive_sync(self) -> VendingMachineData:
        self.vending_machine.status = "inactive"
        self.vending_machine.save()

        return VendingMachineData(
            vending_machine=self.vending_machine,
            is_active=False
        )

    def is_active(self) -> bool:
        try:
            self._machine_info()

            return True
        except requests.exceptions.ConnectionError:
            return False

    def get_request(self, sub_url: str) -> requests.Response:
        r = super()._request(
            method=requests.get,
            url=self.VENDING_MACHINE_URL,
            sub_url=sub_url,
        )

        return r
    
    def post_request(self, sub_url: str, data: dict, files: dict = {}) -> requests.Response:
        r = super()._request(
            method=requests.post,
            url=self.VENDING_MACHINE_URL,
            sub_url=sub_url,
            data=data,
            files=files
        )

        return r
    
    def put_request(self, sub_url: str, data: dict, files: dict = {}) -> requests.Response:
        r = super()._request(
            method=requests.put,
            url=self.VENDING_MACHINE_URL,
            sub_url=sub_url,
            data=data,
            files=files
        )

        return r
    
    def delete_request(self, sub_url: str) -> requests.Response:
        r = super()._request(
            method=requests.delete,
            url=self.VENDING_MACHINE_URL,
            sub_url=sub_url
        )

        return r

    def _machine_info(self) -> None:
        response = self.get_request(self.URLS["info"])

        self.vending_machine.name = response["name"]
        self.vending_machine.address = response["address"]
        self.vending_machine.status = "active"

        self.vending_machine.save()

        return self.vending_machine

    @classmethod
    def get_syncronized_vending_machines(cls) -> List[VendingMachineData]:
        services = []
        
        for vending_machine in models.VendingMachineModel.objects.all():
            services.append(
                cls(vending_machine).sync()
            )

        return services
