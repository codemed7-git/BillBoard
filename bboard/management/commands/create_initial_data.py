from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from bboard.models import Bb, Rubric


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
        return user

    def _ensure_sample_ads(self, admin_user, regular_user):
        if Bb.objects.exists():
            return

        samples = [
            {
                'title': 'Велосипед горный',
                'content': 'Отличное состояние, 21 скорость.',
                'price': '15000.00',
                'rubric': 'Транспорт',
                'author': regular_user,
            },
            {
                'title': '1-комнатная квартира',
                'content': 'Сдаётся на длительный срок, центр города.',
                'price': '35000.00',
                'rubric': 'Недвижимость',
                'author': admin_user,
            },
            {
                'title': 'Python-разработчик',
                'content': 'Удалённая работа, Django, PostgreSQL.',
                'price': None,
                'rubric': 'Работа',
                'author': admin_user,
            },
            {
                'title': 'Ремонт ноутбуков',
                'content': 'Диагностика бесплатно, выезд на дом.',
                'price': '500.00',
                'rubric': 'Услуги',
                'author': regular_user,
            },
        ]

        for item in samples:
            rubric = Rubric.objects.get(name=item['rubric'])
            Bb.objects.create(
                title=item['title'],
                content=item['content'],
                price=item['price'],
                rubric=rubric,
                author=item['author'],
                is_active=True,
            )

        self.stdout.write(self.style.SUCCESS(f'Created {len(samples)} sample ads'))

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

        admin_user = self._ensure_user(
            'admin',
            'admin123',
            'admin@example.com',
            is_staff=True,
            is_superuser=True,
        )
        regular_user = self._ensure_user(
            'user',
            '27kafthebest',
            'user@example.com',
        )
        self._ensure_sample_ads(admin_user, regular_user)
