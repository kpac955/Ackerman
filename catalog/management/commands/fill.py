import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def _load_data(file_name):
        # Путь к фикстурам
        path = f"catalog/fixtures/{file_name}"
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def handle(self, *args, **options):
        # 1. Удаление старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2. Загрузка категорий из JSON
        categories_json = self._load_data("categories.json")
        categories_for_create = []
        for item in categories_json:
            categories_for_create.append(Category(pk=item["pk"], **item["fields"]))
        Category.objects.bulk_create(categories_for_create)

        # 3. Загрузка продуктов из JSON
        products_json = self._load_data("products.json")
        products_for_create = []
        for item in products_json:
            category_instance = Category.objects.get(pk=item["fields"]["category"])
            item["fields"]["category"] = category_instance

            products_for_create.append(Product(pk=item["pk"], **item["fields"]))
        Product.objects.bulk_create(products_for_create)

        self.stdout.write(self.style.SUCCESS("База данных успешно пересоздана!"))
