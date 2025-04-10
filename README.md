# Тестовое задание в RocketData

---

## Описание

Проект представляет собой систему управления звеньями цепи поставок электроники. Основные функции:
- Иерархическая структура звеньев
- API-доступ с использованием ключа
- Автоматическое обновление задолженности
- Отправка QR-кода на email
- Админ-интерфейс

## Технологии

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Celery + Redis
- Docker + Docker Compose
- django-celery-beat
- python-dotenv
- WhiteNoise (обслуживание статики)
- qrcode (генерация QR-кодов)

## Установка и запуск

[Инструкция по установке](docs/installation.md)

## Структура проекта

[Структура проекта](docs/structure.md)

## Доступы

- Админ-панель: [http://localhost:18000/admin/](http://localhost:18000/admin/)
- API: [http://localhost:18000/init/api/](http://localhost:18000/init/api/)

## API и примеры запросов

[Список эндпоинтов](docs/api_endpoints.md)