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
- Аутентификация (Token/JWT)
- Тесты

## 🛠 Стек
- Django 5.x
- Django REST Framework
- drf-spectacular (документация)
- django-filter
- JWT
- PostgreSQL

## 🗺 Планы
- Custom user model
- Docker


## 🏁 Запуск
```bash
git clone https://github.com/Bukh-sun/library_api.git
cd library_api
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate
pip install -r requirements.txt
```
установить и запустить PostgreSQL
```bash
cp .env.example .env 
```
открыть .env и заполнить своими значениями (данные подключения к PostgreSQL, SECRET_KEY)
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
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
python manage.py test
```