# Library API

REST API для управления библиотекой (книги, авторы, жанры).  
Учебный проект для изучения Django REST Framework.

## 🚀 Что уже реализовано
- Модели: Author, Genre, Book (связи ForeignKey и ManyToMany)
- Сериализаторы с вложенными полями (`author_detail`, `genres_detail`)
- ViewSet для книг с полным CRUD
- Маршрутизация через DefaultRouter
- Подготовлена база данных SQLite

## 🛠 Стек
- Django 5.x
- Django REST Framework
- drf-spectacular (документация)
- django-filter (планируется)

## 🗺 Планы
- Пагинация и фильтрация
- Аутентификация (Token/JWT)
- Тесты
- Переход на PostgreSQL

## 🏁 Запуск
```bash
git clone ...
cd library_api
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver