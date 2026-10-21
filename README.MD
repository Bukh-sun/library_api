# Library API

REST API для управления библиотекой (книги, авторы, жанры).
Учебный проект для изучения Django REST Framework.

## 🚀 Что уже реализовано
- Модели: Author, Genre, Book (связи ForeignKey и ManyToMany)
- Сериализаторы с вложенными полями
- ViewSet для книг, авторов с полным CRUD, ViewSet для жанров (только чтение) 
- Маршрутизация через DefaultRouter
- База данных на PostgreSQL
- Пагинация и фильтрация
- Аутентификация (JWT)
- Авторизация / permissions / Права доступа: читать могут все, 
создавать — только вошедшие пользователи, редактировать и удалять книгу — только тот, кто её добавил
- Тесты


## 🛠 Стек
- Django 5.x
- Django REST Framework
- drf-spectacular (документация)
- django-filter
- JWT
- PostgreSQL
- Docker

## 🗺 Планы
- Custom user model
- Nginx

## 🏁 Запуск
Нужен установленный Docker (на Windows и macOS — Docker Desktop).
```bash
git clone https://github.com/Bukh-sun/library_api.git
cd library_api
cp .env.example .env
#открыть .env и заполнить своими значениями (данные подключения к PostgreSQL, SECRET_KEY)
docker compose up -d --build
docker compose exec my_app python manage.py createsuperuser
```

### Для разработки: база в Docker, Django из IDE
```bash
docker compose up -d db
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001
```

## 📖 Документация
После запуска доступна интерактивная документация (Swagger):
- http://127.0.0.1:8000/api/docs/

Основные эндпоинты:
- `/api/books/` — книги
- `/api/authors/` — авторы
- `/api/genres/` — жанры (только чтение)
- `/api/token/` — получение JWT-токена

## 🧪 Тесты
```bash
docker compose exec my_app python manage.py test
```