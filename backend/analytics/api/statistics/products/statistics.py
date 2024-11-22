from typing import List

from .services import ProductData


class ProductStockStatistics:
    def __init__(self, data_objects: List[ProductData]) -> None:
        self.data_objects = data_objects

    def product_stock(self) -> List[ProductData]:
        product_stock = []

        for data_object in self.data_objects:
            product_stock.append({
                "vending_machine": data_object.vending_machine,
                "product_stock": data_object.product_stock
            })

        return product_stock
