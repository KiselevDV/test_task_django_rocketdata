## Структура проекта
.
├── config
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker
│   ├── docker-compose.yml
│   └── Dockerfile
├── docs
├── init
│   ├── admin.py
│   ├── api
│   │   ├── authentication.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management
│   │   └── commands
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tasks.py
│   ├── templates
│   │   └── init
│   │       └── nodes_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── staticfiles
    ├── admin
    │   ├── css
    │   ├── fonts
    │   ├── img
    │   └── js
    ├── rest_framework
    │   ├── css
    │   ├── docs
    │   ├── fonts
    │   ├── img
    │   └── js
    └── staticfiles.json

[← Назад к README](../README.md)