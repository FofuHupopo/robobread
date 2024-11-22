from __future__ import annotations

from typing import List

from django.conf import settings

from api.exceptions import ServiceResponseException
from api.vending_machines.vending_machines.services import VendingMachineService
from api.products.models import ProductModel

from .serializers import ProductsInCellSerializer
from .data import ProductsInCellData


PROTOCOL = getattr(settings, "VENDING_MACHINES_PROTOCOL")

URLS = {
    "cells": "products/cell",
    "products_in_cell": "products/cell/{}/products",
    "product_in_cell": "products/cell/{}/products/{}",
}


class ProductsInCellService(VendingMachineService):
    def __init__(self, *args) -> None:
        super().__init__(*args)

        self.update_urls(URLS)

    def active_sync(self) -> ProductsInCellData:
        vending_machine_data = super().active_sync()

        cells = self.get_cells()

        return ProductsInCellData(
            **vending_machine_data.__dict__,
            cells=cells
        )

    def inactive_sync(self) -> ProductsInCellData:
        vending_machine_data = super().inactive_sync()

        return ProductsInCellData(
            **vending_machine_data.__dict__,
            cells=[]
        )

    def get_cells(self) -> List[ProductModel]:
        cells = self.get_request(URLS["cells"])

        for cell in cells:
            cell["products"] = self.get_request(
                URLS["products_in_cell"].format(cell["id"])
            )

        return cells

    def update_cells(self, cells: ProductsInCellSerializer):
        for cell in cells["cells"]:
            print(cell)
            cell_id = cell["id"]

            for product_in_cell in cell["products"]:
                product_in_cell_id = product_in_cell["id"]
                
                self.put_request(
                    URLS["product_in_cell"].format(
                        cell_id,
                        product_in_cell_id
                    ),
                    product_in_cell
                )
