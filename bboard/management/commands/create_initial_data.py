# bboard/management/commands/create_initial_data.py
from django.core.management.base import BaseCommand
from bboard.models import Rubric, Bb
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **options):
        # Создаем рубрики
        rubrics = [
            'Транспорт',
            'Недвижимость',
            'Работа',
            'Услуги',
            'Личные вещи',
            'Для дома и дачи',
            'Разное'
        ]

        for rubric_name in rubrics:
            Rubric.objects.get_or_create(name=rubric_name)

        self.stdout.write(
            self.style.SUCCESS('Successfully created rubrics')
        )

        # Создаем тестовые объявления, если нет пользователя
        if not User.objects.exists():
            user = User.objects.create_user(
                username='admin',
                password='admin123',
                email='admin@example.com'
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully created admin user')
            )
        else:
            user = User.objects.first()