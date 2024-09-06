from __future__ import annotations

from typing import List

from django.conf import settings
from django.forms.models import model_to_dict

from api.exceptions import ServiceResponseException
from api.vending_machines.services import VendingMachineService
from .data import CategoryData, ProductData
from . import models


PROTOCOL = getattr(settings, "VENDING_MACHINES_PROTOCOL")

URLS = {
    "category": "products/category",
    "products": "products/all-product",
    "product_detail": "products/product",
}


class CategoryService(VendingMachineService):
    def __init__(self, *args) -> None:
        super().__init__(*args)

        self.update_urls(URLS)

    def active_sync(self) -> CategoryData:
        vending_machine_data = super().active_sync()

        categories = self.get_categories()

        return CategoryData(
            **vending_machine_data.__dict__,
            categories=categories
        )

    def inactive_sync(self) -> CategoryData:
        vending_machine_data = super().inactive_sync()

        return CategoryData(
            **vending_machine_data.__dict__,
            categories=[]
        )

    def get_categories(self) -> List[models.CategoryModel]:
        return self.get_request(URLS["category"])

    def create_category(self, category: models.CategoryModel) -> models.CategoryModel:
        data = model_to_dict(category)
        files = {
            "image": data.pop("image")
        }
        data.pop("id")

        self.post_request(self.URLS["category"], data, files)
    
    def delete_category(self, category: models.CategoryModel) -> models.CategoryModel:
        category_id = self.get_category_by_sku(category.sku)["id"]

        self.delete_request(f'{self.URLS["category"]}/{category_id}')

    def update_category(self, category: models.CategoryModel) -> models.CategoryModel:
        category_id = self.get_category_by_sku(category.sku)["id"]

        print(category)

        data = model_to_dict(category)
        files = {
            "image": data.pop("image")
        }
        data.pop("id")

        self.put_request(f'{self.URLS["category"]}/{category_id}', data, files)

    def get_category_by_sku(self, sku: str) -> models.CategoryModel:
        categories = self.get_categories()

        for vm_category in categories:
            if vm_category["sku"] == sku:
                return vm_category
            
        raise ServiceResponseException("Category not found", status_code=404)


class ProductService(VendingMachineService):
    def __init__(self, *args) -> None:
        super().__init__(*args)

        self.update_urls(URLS)

    def active_sync(self) -> ProductData:
        vending_machine_data = super().active_sync()

        products = self.get_products()

        return ProductData(
            **vending_machine_data.__dict__,
            products=products
        )

    def inactive_sync(self) -> ProductData:
        vending_machine_data = super().inactive_sync()

        return ProductData(
            **vending_machine_data.__dict__,
            products=[]
        )

    def get_products(self) -> List[models.ProductModel]:
        data = self.get_request(URLS["products"])
        print(data)
        return data

    def create_product(self, product: models.ProductModel) -> models.ProductModel:
        category = CategoryService(
            self.vending_machine
        ).get_category_by_sku(product.category.sku)

        data = model_to_dict(product)
        data["category_id"] = category["id"]

        files = {
            "image": data.pop("image")
        }
        data.pop("id")

        self.post_request(URLS["products"], data, files)

    def delete_product(self, product: models.ProductModel) -> models.ProductModel:
        product_id = self.get_product_by_sku(product.sku)["id"]

        self.delete_request(f'{URLS["products"]}/{product_id}')

    def update_product(self, product: models.ProductModel) -> models.ProductModel:
        old_product = self.get_product_by_sku(product.sku)
        product_id = old_product["id"]

        print(old_product, product.image.url)

        category = CategoryService(
            self.vending_machine
        ).get_category_by_sku(product.category.sku)

        data = model_to_dict(product)
        data["category_id"] = category["id"]

        files = {
            "image": data.pop("image")
        }
        data.pop("id")

        self.put_request(f'{URLS["products"]}/{product_id}', data, files)

    def get_product_by_sku(self, sku: str) -> models.CategoryModel:
        products = self.get_products()

        for vm_product in products:
            if vm_product["sku"] == sku:
                return vm_product

        raise ServiceResponseException("Product not found", status_code=404)
