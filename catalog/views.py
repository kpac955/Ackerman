from django.shortcuts import get_object_or_404, render

from .models import Product


def home(request):
    products = Product.objects.all()

    latest_products = Product.objects.order_by("-created_at")[:5]
    print("Последние 5 товаров:")
    for p in latest_products:
        print(f"ID: {p.id}, Название: {p.name}")

    context = {
        "object_list": products,
    }
    return render(request, "catalog/index.html", context)


def product_detail(request, pk):
    # поиск товара по ID, если не находит - ошибка 404
    product = get_object_or_404(Product, pk=pk)

    context = {
        "object": product,
    }
    return render(request, "catalog/product_detail.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"Имя: {name}, Сообщение: {message}")
    return render(request, "catalog/contacts.html")
