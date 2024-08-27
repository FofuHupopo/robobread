from django.core.management.base import BaseCommand
import random
import json

from api.products.models import CategoryModel, ProductModel, CellModel


DATA_PATH = "api/products/management/commands/faker.json"


class Command(BaseCommand):
    help = 'Fill the database with mock data'

    def handle(self, *args, **options):
        fill_categories()


def fill_categories():
    categories = json.load(open(DATA_PATH))

    for category_data in categories:
        category_instance = CategoryModel.objects.create(
            name=category_data["name"],
            image=category_data["image"]
        )
        
        fill_products(category_instance, category_data.get("products", []))


def fill_products(category: CategoryModel, products_data: list[dict]):
    for product in products_data:
        product_instance = ProductModel.objects.create(
            name=product["name"],
            description=product["description"],
            composition="Мука, вода, соль, масло, яйца, шоколад, сахар",
            sku=product["sku"],
            price=product["price"],
            category=category,
            image=product["image"]
        )
