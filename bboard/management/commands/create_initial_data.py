from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from bboard.models import Rubric


class Command(BaseCommand):
    help = 'Create initial data for the application'

    def _ensure_user(self, username, password, email, *, is_staff=False, is_superuser=False):
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': is_staff,
                'is_superuser': is_superuser,
            },
        )
        user.email = email
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_active = True
        user.set_password(password)
        user.save()
        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(f'{action} user "{username}"'))

    def handle(self, *args, **options):
        rubrics = [
            'Транспорт',
            'Недвижимость',
            'Работа',
            'Услуги',
            'Личные вещи',
            'Для дома и дачи',
            'Разное',
        ]

        for rubric_name in rubrics:
            Rubric.objects.get_or_create(name=rubric_name)

        self.stdout.write(self.style.SUCCESS('Rubrics are ready'))

        self._ensure_user(
            'admin',
            'admin123',
            'admin@example.com',
            is_staff=True,
            is_superuser=True,
        )
        self._ensure_user(
            'user',
            '27kafthebest',
            'user@example.com',
        )
