from django.shortcuts import render

from .models import Product


def home(request):
    # Берем все товары из базы данных
    products = Product.objects.all()

    # Вывод 5 последних товаров
    latest_products = Product.objects.order_by("-created_at")[:5]
    print("Последние 5 товаров:")
    for p in latest_products:
        print(f"ID: {p.id}, Название: {p.name}")

    context = {
        "object_list": products,
    }
    return render(request, "catalog/index.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"Имя: {name}, Сообщение: {message}")
    return render(request, "catalog/contacts.html")

