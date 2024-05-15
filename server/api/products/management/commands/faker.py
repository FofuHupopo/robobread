from django.core.management.base import BaseCommand
from api.products.models import CategoryModel, ProductModel


class Command(BaseCommand):
    help = 'Fill the database with mock data'

    def handle(self, *args, **options):
        fake_categories()


def fake_categories():
    categories = [
        {"name": "круассаны", "image": "categories/default.png"},
        {"name": "пончики", "image": "categories/default.png"},
        {"name": "булочки", "image": "categories/default.png"},
        {"name": "свежий хлеб", "image": "categories/default.png"},
        {"name": "маффины", "image": "categories/default.png"},
    ]

    for category_name in categories:
        category = CategoryModel.objects.create(
            name=category_name["name"],
            image=category_name["image"]
        )
        
        fake_products(category)
        break


def fake_products(category: CategoryModel):
    products = [
        {"name": "Круассан шоколадный", "price": 10000},
        {"name": "Круассан ванильный", "price": 15000},
        {"name": "Круассан сливочный", "price": 10000},
        {"name": "Круассан клубничный", "price": 12000},
        {"name": "Круассан с бананом и клубникой", "price": 20000},
    ]
    
    for product in products:
        ProductModel.objects.create(
            name=product["name"],
            description="Очаровательный круассан с шоколадом, где хрустящие слои теста в объятиях нежного шоколада создают волшебное сочетание вкуса и текстуры. Идеальное сочетание нежности и интенсивного вкуса, которое заставит ваше сердце биться быстрее и заставит вас возвращаться снова и снова.",
            composition="Мука, вода, соль, масло, яйца, шоколад, сахар",
            price=product["price"],
            category=category,
            image="products/default.png"
        )
