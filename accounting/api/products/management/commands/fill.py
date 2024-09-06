from django.core.management.base import BaseCommand
from django.utils.timezone import timedelta
from django.db.utils import IntegrityError

import json

from api.products.models import CategoryModel, ProductModel

DATA_PATH = "api/products/management/commands/data.json"


class Command(BaseCommand):
    help = 'Fill the database with mock data'

    def handle(self, *args, **options):
        fill_categories()


def str_to_timedelta(time_str: str):
    parts = time_str.split()

    if len(parts) == 2:
        days = int(parts[0])
        time = parts[1]
    else:
        days = 0
        time = parts[0]

    hours, minutes, seconds = map(int, time.split(':'))
    
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def fill_categories():
    categories = json.load(open(DATA_PATH))

    for category_data in categories:
        try:
            category_instance = CategoryModel.objects.create(
                name=category_data["name"],
                sku=category_data["sku"],
                image=category_data["image"]
            )

        except IntegrityError:
            continue

        fill_products(category_instance, category_data.get("products", []))


def fill_products(category: CategoryModel, products_data: list[dict]):
    for product in products_data:
        try:
            ProductModel.objects.create(
                name=product["name"],
                description=product["description"],
                composition="Мука, вода, соль, масло, яйца, шоколад, сахар",
                price=product["price"],
                category=category,
                image=product["image"],
                sku=product["sku"],
                expiration_date=str_to_timedelta(product["expiration_date"]),
            )
        except IntegrityError:
            continue
