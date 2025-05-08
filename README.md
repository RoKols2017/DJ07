# 🛰️ Task 2 — Интеграция Telegram-бота с Django API

## 📋 Описание

Этот этап проекта реализует интеграцию Telegram-бота с Django REST API.  
Бот регистрирует пользователей через команду `/`start`/`, отправляя их ID и username на API endpoint Django-проекта.

---

## 🚀 Функциональность

- Команда `/`start`/` в Telegram:
  - Отправляет POST-запрос на `/`api/register`/`
  - Если пользователь новый — бот сообщает об успешной регистрации
  - Если уже зарегистрирован — уведомляет об этом

---

## 🛠️ Установка и запуск

### 1. Клонируй проект и активируй окружение
```bash
git clone <http://github.com/RoKols2017/DJ07>
cd <папка_проекта>
git checkout task-2-telegram-bot

python -m venv venv
source venv/bin/activate  
# Для Windows: venv\Scripts\activate
```

---

### 2. Установи зависимости
```bash
pip install -r requirements.txt
```
---

### 🔐 2.1 Создай файл `/`.env/`

В корне проекта создай файл `/`.env/` и добавь туда токен бота:

```
TELEGRAM_BOT_TOKEN=your_real_bot_token_here
```

---

### 🛠️ 2.2 Установи поддержку `/`.env/`

Установи пакет `/`python-dotenv/`, если он ещё не установлен:

```
pip install python-dotenv
```

Добавь его в файл `/`requirements.txt/`:

```
python-dotenv
```

Если файла `requirements.txt` нет, то:
```bash
pip install django djangorestframework pyTelegramBotAPI
```

---

### 3. Запусти Django API
```bash
python manage.py runserver
```

---

### ⚙️ 4. Укажи токен бота

Токен указывается в файле `/`.env/`. Пример:

```
TELEGRAM_BOT_TOKEN=your_real_bot_token_here
```

В `/`tg_bot.py/` он загружается автоматически через `/`dotenv/`.

---

### 5. Запусти бота
```bash
python tg_bot.py
```

---

## 🧪 Тестирование

1. Открой Telegram и отправь боту `/`start`/`
2. Проверь, что бот отвечает:
   - `✅ Вы успешно зарегистрированы!`
   - или `🔁 Вы уже зарегистрированы.`
3. Проверь базу данных Django — пользователь должен быть создан

---

## 📁 Структура файлов
```
.
├── djangobot/             # Django-проект
│   └── settings.py
├── bot/                   # Django-приложение
│   └── views.py
│   └── models.py
│   └── serializers.py
├── tg_bot.py              # Telegram-бот
├── manage.py
├── /.env/                 # 🔐 Хранит токен бота (НЕ пушить!)
├── /.gitignore/           # Должен содержать строку /.env/
├── /tg_bot.py/            # Бот получает токен из /.env/
└── /requirements.txt/     # Содержит python-dotenv
```

---

## 🧩 Используемые технологии

- Django
- Django REST Framework
- pyTelegramBotAPI
- SQLite (по умолчанию)

---

## 📜 Автор

RoKols2017@gmail.com
