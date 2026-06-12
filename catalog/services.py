from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_by_category(category_id):
    """Возвращает список продуктов в указанной категории с использованием кеша."""

    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    key = f"products_list_category_{category_id}"

    products = cache.get(key)

    if products is None:
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products)

    return products
