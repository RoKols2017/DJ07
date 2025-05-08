import telebot
import requests
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

API_URL = 'http://127.0.0.1:8000/api/register/'  # или через ngrok в проде
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    username = message.from_user.username or ""

    # POST-запрос в Django API
    response = requests.post(API_URL, json={
        "user_id": user_id,
        "username": username
    })

    if response.status_code == 201:
        bot.send_message(message.chat.id, "✅ Вы успешно зарегистрированы!")
    elif response.status_code == 200:
        bot.send_message(message.chat.id, "🔁 Вы уже зарегистрированы.")
    else:
        bot.send_message(message.chat.id, "⚠️ Произошла ошибка регистрации.")

@bot.message_handler(commands=['myinfo'])
def handle_myinfo(message):
    user_id = message.from_user.id
    response = requests.get(API_URL.replace('register', 'myinfo'), params={
        'user_id': user_id
    })

    if response.status_code == 200:
        data = response.json()
        bot.send_message(message.chat.id, f"👤 Ваши данные:\nID: {data['user_id']}\nUsername: {data.get('username')}")
    else:
        bot.send_message(message.chat.id, "❌ Вы не зарегистрированы.")

bot.polling()

