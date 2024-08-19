from __future__ import annotations

import requests

from typing import List, Mapping, Optional
from dataclasses import dataclass

from . import models


URLS = {
    "info": "security/info",
}


@dataclass
class VendingMachineData:
    vending_machine: models.VendingMachineModel = None
    is_active: bool = None


class VendingMachineService:
    def __init__(self, vending_machine: models.VendingMachineModel) -> None:
        self.vending_machine = vending_machine
        self.URLS = dict()

        self.update_urls(URLS)

    def active_sync(self) -> VendingMachineData:
        return VendingMachineData(
            vending_machine=self.vending_machine, is_active=True
        )

    def inactive_sync(self) -> VendingMachineData:
        return VendingMachineData(
            vending_machine=self.vending_machine,
            is_active=False
        )
    
    def sync(self) -> VendingMachineData:
        if self.is_active():
            data_object = self.active_sync()
            data_object.is_active = True

            self.vending_machine.status = "active"
        else:
            data_object = self.inactive_sync()
            data_object.is_active = False

            self.vending_machine.status = "inactive"
        
        self.vending_machine.save()
        data_object.vending_machine = self.vending_machine

        return data_object

    def is_active(self) -> bool:
        try:
            self._machine_info()
            return True

        except requests.exceptions.ConnectionError:
            return False

    def update_urls(self, urls: Mapping[str, str]) -> None:
        self.URLS.update(urls)

    def _request(self, sub_url: str) -> requests.Response:
        url = f"http://{self.vending_machine.ip_address}/api/{sub_url}"
        r = requests.get(url)

        if r.status_code not in (200, 201):
            raise ValueError(f"Bad status code, got {r.status_code}")

        return r.json()

    def _machine_info(self) -> None:
        response = self._request(self.URLS["info"])

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
        