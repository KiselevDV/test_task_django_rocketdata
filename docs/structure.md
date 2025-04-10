## Структура проекта
```
.
├── config/                 # Конфигурация Django и Celery
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker/                 # Docker-конфигурация
│   ├── docker-compose.yml
│   └── Dockerfile
├── docs/                   # Документация проекта
│   ├── api_endpoints.md
│   ├── installation.md
│   └── structure.md
├── init/                   # Основное Django-приложение
│   ├── admin.py
│   ├── api/                # DRF: сериализаторы, представления, permissions
│   │   ├── authentication.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management/         # Команды manage.py
│   │   └── commands/
│   │       └── test_data.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tasks.py            # Celery задачи
│   ├── templates/
│   │   └── init/
│   │       └── nodes_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── staticfiles/            # Собранная статика
    ├── admin/
    ├── rest_framework/
    └── staticfiles.json
```

[← Назад к README](../README.md)