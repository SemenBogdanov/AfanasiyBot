import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(str(token))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Проверка пользователя на знакомство
    bot.send_message(message.chat.id, "Вот что я могу!", reply_markup=welcome_func())


def welcome_func():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Последние новости", callback_data="news"))
    markup.add(InlineKeyboardButton("Погода", callback_data="get_weather"),
               InlineKeyboardButton("Курс валют", callback_data="course_exchange"))
    markup.add(InlineKeyboardButton("Курс по коду валюты", callback_data="course_exchange2"))
    markup.add(InlineKeyboardButton("Добавить день рождение", callback_data="course_exchange"))
    markup.add(InlineKeyboardButton("Дни рождения сегодня", callback_data="course_exchange"))
    markup.add(InlineKeyboardButton("Дни рождения в ближайший месяц", callback_data="course_exchange"))
    markup.add(InlineKeyboardButton("Отслеживание ПочтаРоссии", callback_data="get_Rpo"))
    return markup


@bot.message_handler(content_types=['text'])
def function_name(message):
    bot.send_message(message.chat.id, "Вот что я могу!", reply_markup=welcome_func())


print("бот запущен!")

bot.polling()
