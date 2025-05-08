# 🧩 Task 1 — Django REST API: Регистрация пользователей Telegram

## 📋 Описание

В этом задании реализуется базовый Django REST API для регистрации пользователей Telegram.  
Регистрация выполняется через POST-запрос на эндпоинт ///api/register///.  
Пользователи сохраняются в базу данных.

---

## 🚀 Функциональность

- POST-эндпоинт ///api/register///:
  - Принимает JSON с полями ///user_id/// и ///username///
  - Создаёт нового пользователя или сообщает, что он уже зарегистрирован
  - Возвращает JSON-ответ с данными пользователя или сообщением

---

## 🛠️ Установка и запуск

### 1. Клонируй проект и создай виртуальное окружение
```bash
git clone https://ginhub.com/RoKols2017/DJ07
cd <папка_проекта>

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

### 2. Установи зависимости
```bash
pip install django djangorestframework
```

---

### 3. Создай Django-проект и приложение
```bash
django-admin startproject djangobot .
python manage.py startapp bot
```

---

### 4. Настрой ///INSTALLED_APPS/// в ///djangobot/settings.py///
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'bot',
]
```

---

### 5. Создай модель ///TelegramUser/// в ///bot/models.py///
```python
from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"///{self.username} ({self.user_id})///"
```

---

### 6. Примени миграции
```bash
python manage.py makemigrations bot
python manage.py migrate
```

---

### 7. Создай сериализатор ///TelegramUserSerializer/// в ///bot/serializers.py///
```python
from rest_framework import serializers
from .models import TelegramUser

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'
```

---

### 8. Реализуй API view в ///bot/views.py///
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from .serializers import TelegramUserSerializer

@api_view(['POST'])
def register_user(request):
    data = request.data
    user, created = TelegramUser.objects.get_or_create(
        user_id=data['user_id'],
        defaults={'username': data.get('username', '')}
    )
    serializer = TelegramUserSerializer(user)
    if created:
        return Response(serializer.data, status=201)
    return Response(serializer.data)
```

---

### 9. Настрой роутинг в ///djangobot/urls.py///
```python
from django.contrib import admin
from django.urls import path
from bot.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user),
]
```

---

### 🔬 10. Тестирование API

1. Запусти сервер:
```bash
python manage.py runserver
```

2. Используй Postman или расширение Boomerang:
   - Метод: POST  
   - URL: http://127.0.0.1:8000/api/register/  
   - Headers:  
     - Key: ///Content-Type///  
     - Value: ///application/json///
   - Body:
```json
{
  "user_id": 123456,
  "username": "cooluser"
}
```

---

## 📁 Структура проекта

```
.
├── djangobot/
│   └── settings.py
│   └── urls.py
├── bot/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
├── manage.py
```

---

## 🧩 Используемые технологии

- Django
- Django REST Framework
- SQLite (по умолчанию)

---

## 📜 Автор

RomEfak@gmail.com
