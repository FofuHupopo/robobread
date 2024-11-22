from __future__ import annotations

from typing import List

from django.conf import settings
from django.forms.models import model_to_dict

from api.exceptions import ServiceResponseException
from api.vending_machines.vending_machines.services import VendingMachineService
from api.products.models import CategoryModel

from .data import CategoryData


PROTOCOL = getattr(settings, "VENDING_MACHINES_PROTOCOL")

URLS = {
    "category": "products/category",
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

    def get_categories(self) -> List[CategoryModel]:
        return self.get_request(URLS["category"])

    def create_category(self, category: CategoryModel) -> CategoryModel:
        data = model_to_dict(category)
        files = {
            "image": data.pop("image")
        }
        data.pop("id")

        self.post_request(self.URLS["category"], data, files)
    
    def delete_category(self, category: CategoryModel) -> CategoryModel:
        category_id = self.get_category_by_sku(category.sku)["id"]

        self.delete_request(f'{self.URLS["category"]}/{category_id}')

    def update_category(self, category: CategoryModel) -> CategoryModel:
        category_id = self.get_category_by_sku(category.sku)["id"]

        print(category)

        data = model_to_dict(category)
        files = {
            "image": data.pop("image")
        }
        data.pop("id")

        self.put_request(f'{self.URLS["category"]}/{category_id}', data, files)

    def get_category_by_sku(self, sku: str) -> CategoryModel:
        categories = self.get_categories()

        for vm_category in categories:
            if vm_category["sku"] == sku:
                return vm_category
            
        raise ServiceResponseException("Category not found", status_code=404)
