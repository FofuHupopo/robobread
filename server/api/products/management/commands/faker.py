import json
import random
from django.core.management.base import BaseCommand
from django.utils import timezone

from api.products.models import (
    CategoryModel, ProductModel, CellModel, ProductInCellModel
)


FAKER_PATH = "api/products/management/commands/faker.json"


class Command(BaseCommand):
    help = 'Fill the database with mock data'

    def handle(self, *args, **options):
        fake_categories()


def fake_categories():
    categories = json.load(open(FAKER_PATH))

    for category_data in categories:
        category_instance = CategoryModel.objects.create(
            name=category_data["name"],
            image=category_data["image"]
        )
        
        fake_products(category_instance, category_data.get("products", []))


def fake_products(category: CategoryModel, products_data: list[dict]):
    for product in products_data:
        product_instance = ProductModel.objects.create(
            name=product["name"],
            description=product["description"],
            composition="Мука, вода, соль, масло, яйца, шоколад, сахар",
            sku=product["sku"],
            price=product["price"],
            category=category,
            image=product["image"],
            expiration_date=timezone.timedelta(days=3)
        )

        for cell in product["cells"]:
            max_count = product["max_count"]

            cell = CellModel.objects.create(
                number=cell,
                max_count=max_count,
                product=product_instance
            )

            count = random.randint(0, max_count)

            for _ in range(count):
                cell.add_product(
                    expiration_date=timezone.timedelta(days=3)
                )
