from typing import List
from dataclasses import dataclass

from api.core.services import VendingMachineService, VendingMachineData
from .. import models
from .data import ProductData


URLS = {
    "product_stock": "products/all-product",
}


class ProductStockService(VendingMachineService):
    def __init__(self, vending_machine: models.VendingMachineModel) -> None:
        super().__init__(vending_machine)

        self.update_urls(URLS)
    
    def active_sync(self) -> ProductData:
        data_object = ProductData()

        data_object.product_stock = self._sync_product_stocks()

        return data_object

    def inactive_sync(self) -> VendingMachineData:
        return ProductData(
            product_stock=models.ProductStockModel.objects.filter(
                vending_machine=self.vending_machine
            ),
        )

    def _sync_product_stocks(self) -> List[models.ProductStockModel]:
        response = self._request(self.URLS["product_stock"])

        product_stock = []
        used_product_ids = []

        for product in response:
            quantity = 0
            max_quantity = 0

            for cell in product["cells"]:
                quantity += cell["count"]
                max_quantity += cell["max_count"]

            product_stock_instance = models.ProductStockModel.objects.get_or_create(
                vending_machine=self.vending_machine,
                product_id=product["id"],
            )[0]

            product_stock_instance.product_name = product["name"]
            product_stock_instance.quantity = quantity
            product_stock_instance.max_quantity = max_quantity

            product_stock_instance.save()

            product_stock.append(product_stock_instance)
            used_product_ids.append(product["id"])

        models.ProductStockModel.objects.filter(
            vending_machine=self.vending_machine,
        ).exclude(
            product_id__in=used_product_ids
        ).delete()

        return product_stock
