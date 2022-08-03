# api_yatube
api_yatube
Описание проекта:
    В этом проекте была написана Api часть для проекта yatube Мини-социальная сеть.

Технологии:
    Python, Django, Django Rest Framework

Запуск проекта в dev-режиме
1. Клонировать репозиторий и перейти в него в командной строке.
2. Установите и активируйте виртуальное окружение.
```
    Для Linux/Mac:
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip

    Для пользователей Windows:
    python -m venv venv
    source venv/Scripts/activate
    python -m pip install --upgrade pip
```
3. Установить зависимости из файла requirements.txt
```
    pip install -r requirements.txt
```
4. Выполнить миграции:
```
    python3 manage.py migrate
```
5. Создать супер=пользователя: 
```
    python3 manage.py createsuperuser
```
6. Запустить проект:
```
    python3 manage.py runserver
```
Пример запросов:
По умолчанию для неавторизованных пользователей проект доступен только для чтения.
```
api/v1/posts/ - получение списка всех постов
api/v1/posts/{id}/ - получение поста
api/v1/groups/ - получение списка всех групп
api/v1/groups/{id}/ - получение группы
api/v1/{post_id}/comments/ - получение списка всех комментариев под определенным постом
api/v1/{post_id}/comments/{id}/ - получение комментария
```