# Установка и запуск

## 1. Клонировать репозиторий

```bash
git clone https://github.com/yourusername/test-task-django-rocketdata.git
cd test-task-django-rocketdata
```

## 2. Запуск через Docker

```bash
cd docker
docker compose up --build
```

## 3. Миграции, создание суперпользователя и заполнение БД данными

```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py test_data
```

[← Назад к README](../README.md)