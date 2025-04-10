import secrets

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


class SupplyChainNode(models.Model):
    """Звено сети по продаже электроники"""
    name = models.CharField(max_length=50, verbose_name='Название')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, verbose_name='Адрес')
    products = models.ManyToManyField(
        'Product', blank=True, related_name='nodes', verbose_name='Продукты')
    supplier = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='clients', verbose_name='Поставщик')
    debt = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
        ordering = ('name',)
        indexes = [models.Index(fields=['supplier']),]

    def __str__(self):
        return self.name

    @property
    def level(self):
        """Уровень иерархии текущего звена (0 — завод)"""
        level = 0
        current = self.supplier
        visited = set()
        while current:
            if current.id in visited:
                break
            visited.add(current.id)
            level += 1
            current = current.supplier
        return level

    def get_level_display(self):
        return int(self.level)
    get_level_display.short_description = 'Уровень'

    def clean(self):
        super().clean()
        if self.supplier == self:
            raise ValidationError('Звено не может быть своим поставщиком')

        visited = {self.pk}
        current = self.supplier
        while current:
            if current.pk in visited:
                raise ValidationError('Обнаружена циклическая ссылка в цепочке поставщиков')
            visited.add(current.pk)
            current = current.supplier


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-release_date',)

    def __str__(self):
        return f'{self.name} ({self.model})'


class Address(models.Model):
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=30, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        # indexes = [models.Index(fields=['city'])]

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Employee(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=25, verbose_name='Телефон', validators=[MinLengthValidator(7)])
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    # node не должна быть null или blank
    node = models.ForeignKey(
        SupplyChainNode, on_delete=models.CASCADE, related_name='employees', verbose_name='Звено сети')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.node.name})'

    @property
    def is_authenticated(self):
        return True


class APIKey(models.Model):
    key = models.CharField(max_length=128, unique=True, editable=False, verbose_name='Ключ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    node = models.OneToOneField(
        SupplyChainNode, on_delete=models.CASCADE, related_name='api_key', verbose_name='Звено сети')

    class Meta:
        verbose_name = 'API ключ'
        verbose_name_plural = 'API ключи'

    def __str__(self):
        return f'{self.node.name} API Key'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)
        super().save(*args, **kwargs)
