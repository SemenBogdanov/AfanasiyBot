import os
import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# token = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(str(token))


def boss(call):
    bot.send_message(call.message.chat.id, "Скатин Алексей Владимирович")
    bot.send_photo(call.message.chat.id, 'https://www.pochta.ru/documents/10231/5165333252/Скатин.jpg/'
                                         '45182499-3866-4dac-818d-a62c9d35114c?t=1604668843046')
    bot.send_message(call.message.chat.id, "Вот ссылка на сайт. На всякий случай! \n "
                                           "https://www.pochta.ru/management/skatin-alexey")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Приветственное сообщение!
    bot.send_message(message.chat.id, "Привет! "
                                      "Я бот Афанасий! Могу тебе помочь решить все проблемы! "
                                      "На всякий случай расскажу что я умею: ", reply_markup=welcome_func())


def welcome_func():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Кто руководитель БЭК в АУП?", callback_data="boss"))
    markup.add(InlineKeyboardButton("Как согласовывать наших клиентов?", callback_data="how_clients"))
    return markup


def how_clients_f(call):
    bot.send_message(call.message.chat.id, "Вы отправляете список клиентов с названием и ИНН на территориального "
                                           "управляющего. Он делает сверку с активной базой Почты России и отправляет "
                                           "ответ о согласовании и не согласовании клиентов. (если клиент не работает "
                                           "с Почтой России - клиент согласовывается, если клиент совершает отгрузки "
                                           "через прямой договор с Почтой - отказываем в согласовании данного клиента)")
    bot.send_message(call.message.chat.id, "Может хотите узнать что-то еще?")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "boss":
        boss(call)
    elif call.data == "how_clients":
        how_clients_f(call)
    else:
        call.message.chat.id = "Не совсем понял, что было выбрано..."


@bot.message_handler(content_types=['text'])
def function_name(message):
    bot.send_message(message.chat.id, "Вот что я могу!", reply_markup=welcome_func())


print("бот запущен!")

bot.polling()
