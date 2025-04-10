# test-task-django-rocketdata

## Описание

Проект представляет собой систему управления звеньями сети поставок электроники, в которой реализована иерархия, API-доступ по ключу, автоматическое изменение задолженности, отправка QR-кода на почту и админ-интерфейс.

## Стек технологий

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Celery + Redis
- Docker + Docker Compose
- django-celery-beat
- dotenv
- WhiteNoise (для отдачи статики)
- qrcode (генерация QR-кодов)

## Установка и запуск

[Установка и запуск](docs/installation.md)

## Структура проекта

[Структура проекта](docs/structure.md)

## Доступы

Админ-панель: http://localhost:18000/admin/

API: http://localhost:18000/init/api/

## API и примеры запросов

[API и примеры запросов](docs/api_endpoints.md)