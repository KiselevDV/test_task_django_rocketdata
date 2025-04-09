import random

from decimal import Decimal
from django.core.management.base import BaseCommand

from init.models import SupplyChainNode, Product, Address, Employee


class Command(BaseCommand):
    help = 'Заполнить БД тестовыми данными'

    def handle(self, *args, **kwargs):
        addresses = [
            Address.objects.create(country='Корея', city='Сувон', street='Кенги-до', house_number='443-742'),
            Address.objects.create(country='Китай', city='Чаоян', street='Стоун Уорлд Билдинг', house_number='12'),
            Address.objects.create(country='Россия', city='Москва', street='Атлант-Парк', house_number='29'),
            Address.objects.create(country='Беларусь', city='Минск', street='ул. Притыцкого', house_number='23А'),
            Address.objects.create(country='Беларусь', city='Минск', street='пр-т Независимости', house_number='179'),
            Address.objects.create(country='Беларусь', city='Минск', street='пр. Дзержинского', house_number='8'),
        ]
        self.stdout.write(self.style.SUCCESS('Адреса созданы'))

        products = [
            Product.objects.create(name='Телефон', model='Galaxy F55', release_date='2025-01-01'),
            Product.objects.create(name='Телефон', model='Galaxy M55', release_date='2025-01-02'),
            Product.objects.create(name='Телефон', model='Galaxy A16', release_date='2025-01-03'),
            Product.objects.create(name='Телефон', model='Galaxy S24', release_date='2025-01-04'),
            Product.objects.create(name='Телефон', model='Galaxy A36', release_date='2025-01-05'),
            Product.objects.create(name='Телефон', model='Redmi A5', release_date='2025-01-06'),
            Product.objects.create(name='Телефон', model='Redmi Note 14S', release_date='2025-01-06'),
            Product.objects.create(name='Телефон', model='Redmi Note 14', release_date='2025-01-07'),
            Product.objects.create(name='Телефон', model='Redmi Note 13', release_date='2025-01-08'),
            Product.objects.create(name='Телефон', model='Redmi Note 14 Pro+', release_date='2025-01-09'),
            Product.objects.create(name='Телефон', model='POCO M7 Pro', release_date='2025-01-10'),
        ]
        self.stdout.write(self.style.SUCCESS('Продукты созданы'))

        node1 = SupplyChainNode.objects.create(
            name='Самсунг Электроникс Компани (Завод)',
            email='head@samsung.com',
            address=addresses[0],
            debt=Decimal('1000.00')
        )
        node2 = SupplyChainNode.objects.create(
            name='Сяоми Корпорейшн (Завод)',
            email='head@xiaomi.com',
            address=addresses[1],
            debt=Decimal('1000.00')
        )
        node3 = SupplyChainNode.objects.create(
            name='DNS (Дистрибьютор)',
            email='head@dns.ru',
            address=addresses[2],
            supplier=node1,
            debt=Decimal('500.00')
        )
        node4 = SupplyChainNode.objects.create(
            name='NEWTON (Дилерский центр)',
            email='head@newton.by',
            address=addresses[3],
            supplier=node2,
            debt=Decimal('1500.00')
        )
        node5 = SupplyChainNode.objects.create(
            name='SILA (Крупная розничная сеть)',
            email='head@sila.by',
            address=addresses[4],
            supplier=node3,
            debt=Decimal('1500.00')
        )
        node6 = SupplyChainNode.objects.create(
            name='5element (Крупная розничная сеть)',
            email='head@5element.by',
            address=addresses[5],
            supplier=node2,
            debt=Decimal('1500.00')
        )
        self.stdout.write(self.style.SUCCESS('Звенья сети созданы'))

        node1.products.add(products[0], products[1], products[2], products[3], products[4])
        node2.products.add(products[5], products[6], products[7], products[8], products[9])
        self.stdout.write(self.style.SUCCESS('Продукты связаны с сетями'))

        first_names = [
            'Alexander', 'Ivan', 'Dmitry', 'Sergey', 'Maxim', 'Andrey', 'Victor', 'Petr', 'Evgeny',
            'Roman', 'Vladimir', 'Nikita', 'Konstantin', 'Roman', 'Artem', 'Oleg', 'Stanislav',
            'Timur', 'Anatoly', 'Mikhail'
        ]
        last_names = ['Petrov', 'Ivanov', 'Sidorov', 'Kuznetsov', 'Morozov', 'Smirnov', 'Fedorov',
                      'Lebedev', 'Zakharov', 'Vasilyev', 'Belov', 'Kozlov', 'Novikov', 'Timofeev',
                      'Gorbunov', 'Popov', 'Mikhaylov', 'Grigoryev', 'Chernov', 'Baranov'
                      ]

        for i in range(50):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f'{first_name.lower()}.{last_name.lower()}@gmail.com'
            node = random.choice([node1, node2, node3, node4, node5, node6])
            is_active = random.choice([True, False])
            Employee.objects.create(
                first_name=first_name, last_name=last_name, email=email, node=node, is_active=is_active
            )

        self.stdout.write(self.style.SUCCESS('Сотрудники созданы'))
