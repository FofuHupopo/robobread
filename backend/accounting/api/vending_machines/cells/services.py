from __future__ import annotations

from typing import List

from django.conf import settings
from dataclasses import asdict

from api.vending_machines.vending_machines.services import VendingMachineService

from .data import CellData, CreateCellData, UpdateCellData


PROTOCOL = getattr(settings, "VENDING_MACHINES_PROTOCOL")

URLS = {
    "cells": "products/cell",
}


class ProductService(VendingMachineService):
    def __init__(self, *args) -> None:
        super().__init__(*args)

        self.update_urls(URLS)

    def active_sync(self) -> CellData:
        vending_machine_data = super().active_sync()

        cells = self.get_cells()

        return CellData(
            **vending_machine_data.__dict__,
            cells=cells
        )

    def inactive_sync(self) -> CellData:
        vending_machine_data = super().inactive_sync()

        return CellData(
            **vending_machine_data.__dict__,
            cells=[]
        )

    def get_cells(self) -> List[CellData]:
        data = self.get_request(URLS["cells"])
        return data
    
    def create_cell(self, cell_data: CreateCellData):
        self.post_request(URLS["cells"], asdict(cell_data))

    def delete_cell(self, cell_id: int):
        self.delete_request(f'{URLS["cells"]}/{cell_id}')

    def update_cell(self, cell_id: int, cell_data: UpdateCellData):
        self.put_request(f'{URLS["cells"]}/{cell_id}', asdict(cell_data))
