import requests
from bs4 import BeautifulSoup as b
import random
import telebot

TOKEN = '8726928085:AAGSQIO4u0U3Z3lhoeM8ymcl23IReW1G6W4'
bot = telebot.TeleBot(TOKEN)

def get_jokes():
    url = 'https://www.anekdot.ru/last/good'
    try:
        r = requests.get(url)
        soup = b(r.text, 'html.parser')
        return [d.text for d in soup.find_all('div', class_='text')]
    except Exception as e:
        print(f"Ошибка при получении шуток: {e}")
        return ["Упс, не удалось загрузить шутки. Попробуй позже!"]

jokes = get_jokes()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Пришли мне любое число, и я отправлю тебе случайную шутку.")

@bot.message_handler(content_types=['text'])
def send_joke(message):
    if message.text.isdigit():
        bot.send_message(message.chat.id, random.choice(jokes))
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введи просто число!")

print("Бот успешно запущен и готов к работе...")
bot.polling(none_stop=True)