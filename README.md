# 🧠 Task 3 — Полная интеграция Django API и Telegram-бота

## 📋 Описание

В этом задании реализуется финальная интеграция между Django REST API и Telegram-ботом:  
бот получает информацию о пользователе по команде ```/myinfo``` через GET-запрос.  
Также настраивается CORS для безопасной работы API.

---

## 🚀 Функциональность

- GET-эндпоинт ```api/myinfo```:
  - Принимает ```user_id``` через параметры запроса
  - Возвращает JSON-данные пользователя, если он зарегистрирован
  - Возвращает ошибку, если пользователь не найден
- Бот-команда ```/myinfo```:
  - Отправляет запрос к API
  - Возвращает ID и username пользователя или сообщение об ошибке
- Поддержка CORS для внешнего доступа к API

---

## 🛠️ Установка и запуск

### 1. Переключись на ветку
```bash
git checkout task-3-full-integration
```

---

### 2. Установи зависимости
```bash
pip install django djangorestframework pyTelegramBotAPI python-dotenv django-cors-headers
```

---

### 3. Настрой CORS в ```settings.py```

#### Добавь в ```INSTALLED_APPS```:
```python
INSTALLED_APPS += [
    'corsheaders',
]
```

#### Добавь в начало ```MIDDLEWARE```:
```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # остальные middlewares...
]
```

#### Добавь в конец ```settings.py```:
```python
CORS_ALLOW_ALL_ORIGINS = True  # Только для разработки
```

---

## 🧬 API: GET ```api/myinfo```

### Пример запроса:
```
GET http://127.0.0.1:8000/api/myinfo/?user_id=123456
```

### Пример ответа:
```json
{
  "user_id": 123456,
  "username": "cooluser",
  "created_at": "2025-05-07T10:00:00Z"
}
```

Если пользователь не найден:
```json
{
  "error": "Пользователь не зарегистрирован"
}
```

---

## 🤖 Команда ```/myinfo``` в боте

В файле ```tg_bot.py``` реализована команда:
```python
@bot.message_handler(commands=['myinfo'])
def handle_myinfo(message):
    user_id = message.from_user.id
    response = requests.get(API_URL.replace("register", "myinfo"), params={
        "user_id": user_id
    })

    if response.status_code == 200:
        data = response.json()
        bot.send_message(message.chat.id, f"👤 Ваши данные:\nID: {data['user_id']}\nUsername: {data.get('username')}")
    else:
        bot.send_message(message.chat.id, "❌ Вы не зарегистрированы.")
```

---

## 🔐 Токен Telegram-бота

Хранится в файле ```.env```:
```
TELEGRAM_BOT_TOKEN=your_real_bot_token
```

Подключение через ```dotenv```:
```python
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
```

Файл ```.env``` добавлен в ```.gitignore```

---

## 📁 Структура проекта
```
.
├── /.env/                  # Секреты
├── /tg_bot.py/             # Telegram-бот
├── /bot/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
├── /djangobot/
│   ├── settings.py
│   ├── urls.py
└── manage.py
```

---

## 🧪 Тестирование

1. Зарегистрируй пользователя командой /start
2. Отправь боту /myinfo — получишь данные
3. Удали пользователя из базы — протестируй обработку ошибки
4. Проверь CORS через внешние запросы (например, frontend)

---

## 📜 Автор

RoKols2017@gmail.com
