# Ackerman — Магазин электроники

Учебный проект на Django в рамках курса по веб-разработке. Приложение представляет собой каталог товаров с возможностью просмотра информации и формой обратной связи.

## Функционал
* **Главная страница:** Вывод списка товаров (в разработке).
* **Контакты:** Страница с контактной информацией и формой обратной связи.
* **Обработка данных:** Сбор данных из формы контактов и вывод их в консоль сервера.
* **Стилизация:** Использование Bootstrap 5 для адаптивного интерфейса.
* **ORM и Базы данных:** Реализованы модели Category и Product с настроенными связями (ForeignKey) и мета-данными.
* **Автоматизация (Custom Commands):** Создана кастомная команда `fill` для автоматической очистки и заполнения БД.
* **Качество кода:** Интегрированы линтеры и форматтеры (Black, isort, flake8) для соблюдения стандартов PEP8.


## Технологии
* Python 3.13
* Django 4.2+
* Bootstrap 5
* PostgreSQL

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/kpac955/Ackerman.git
   

2. **Создайте и активируйте виртуальное окружение:**
    ```bash 
    python -m venv venv
     Для Windows:
    venv\Scripts\activate
    ```
3. **Установка зависимостей:**
    ```bash
   pip install -r requirements.txt
    ```
4. **Миграции и подготовка БД: Убедитесь, что у вас создана база данных в PostgreSQL, затем выполните:**
    ```bash
   python manage.py migrate
    ```
5. **Заполнение базы данными (команда fill):**
    ```bash
   python manage.py fill
    ```
6. **Запустите сервер:**
    ```bash
   python manage.py runserver
    ```
    
### Демонстрация работы в Django Shell
![Создание объектов](https://github.com/kpac955/Ackerman/blob/home_work_22_final/screenshots/django_shell_create.png?raw=true)


![Просмотр объектов](https://github.com/kpac955/Ackerman/blob/home_work_22_final/screenshots/django_shell_query_all.png?raw=true)


![Фильтрация и обновление](https://github.com/kpac955/Ackerman/blob/home_work_22_final/screenshots/django_shell_filter_update.png?raw=true)

