from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Rubric(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Рубрика')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bboard:detail', kwargs={'pk': self.pk})