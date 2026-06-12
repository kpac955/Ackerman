from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает права'

    def handle(self, *args, **options):
        # 1. Создаем группу
        moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )

        # 2. Получаем тип контента для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # 3. Список прав
        permissions_list = [
            "can_unpublish_product",
            "delete_product",
        ]

        for perm_code in permissions_list:
            try:
                perm = Permission.objects.get(
                    codename=perm_code, content_type=content_type
                )
                moderator_group.permissions.add(perm)
                self.stdout.write(
                    self.style.SUCCESS(f"Право {perm_code} добавлено группе")
                )
            except Permission.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Право {perm_code} не найдено. Проверь миграции!")
                )

        self.stdout.write(self.style.SUCCESS("Настройка группы завершена!"))
