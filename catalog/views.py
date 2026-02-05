from django.shortcuts import render


# Главная страница
def home(request):
    return render(request, "catalog/index.html")


# Функция для страницы контактов
def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(f"Новая заявка: {name}, Почта: {email}, Текст: {message}")

    return render(request, "catalog/contacts.html")
