import os
import requests
import dictionary_answer as da
import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = os.environ.get('BOT_TOKEN')
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
                                      "Я бот Афанасий! Могу помочь ответить на следующие вопросы:", reply_markup=welcome_func())


def coop():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("1. На какие услуги предоставляется скидка?", callback_data="menu2_cb_q_0"))
    markup.add(InlineKeyboardButton("2. Каким образом предоставляется скидка?", callback_data="menu2_cb_q_1"))
    markup.add(InlineKeyboardButton("3. По каким ценам продавать?", callback_data="menu2_cb_q_2"))
    markup.add(InlineKeyboardButton("4. Как согласовывать наших клиентов?", callback_data="menu2_cb_q_3"))
    markup.add(InlineKeyboardButton("5. Когда будет выдача?", callback_data="menu2_cb_q_4"))
    markup.add(InlineKeyboardButton("6. Весы, ОКВЭД - обязательные условия?", callback_data="menu2_cb_q_5"))
    markup.add(InlineKeyboardButton("7. Вы предосте упаковку?", callback_data="menu2_cb_q_6"))
    markup.add(
        InlineKeyboardButton("8. Забираете отправления или их нужно носить на Почту?", callback_data="menu2_cb_q_7"))
    markup.add(InlineKeyboardButton("9. Как работать с претензиями?", callback_data="menu2_cb_q_8"))
    return markup


@bot.callback_query_handler(func=lambda call: call.data.startswith('menu2_'))
def callback_query(call):
    if call.data == "menu2_cb_q_0":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
        # bot.send_message(call.message.chat.id, call.data)
    elif call.data == "menu2_cb_q_1":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
        # bot.send_message(call.message.chat.id, call.data)
    elif call.data == "menu2_cb_q_2":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    elif call.data == "menu2_cb_q_3":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    elif call.data == "menu2_cb_q_4":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    elif call.data == "menu2_cb_q_5":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    elif call.data == "menu2_cb_q_6":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    elif call.data == "menu2_cb_q_7":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    elif call.data == "menu2_cb_q_8":
        bot.send_message(call.message.chat.id, da.coooperations_agreement_1[int(call.data[-1])])
    else:
        bot.send_message(call.message.chat.id, "Не совсем понял, что было выбрано...")


def welcome_func():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Как стать партнером Почты России?", callback_data="menu1_partner_cb"))
    markup.add(InlineKeyboardButton("Настройка работы", callback_data="menu1_adj_cb"))
    markup.add(InlineKeyboardButton("Договорные отношения", callback_data="menu1_relation_with_agr"))
    markup.add(InlineKeyboardButton("Маркетинг и продвижение", callback_data="menu1_marketSMM_cb"))
    markup.add(InlineKeyboardButton("Налогообложение", callback_data="menu1_taxes_cb"))
    markup.add(InlineKeyboardButton("Выдача посылок в ПВЗ", callback_data="menu1_takeout_cb"))
    markup.add(InlineKeyboardButton("Условия сотрудничества", callback_data="menu1_coop_cb2"))
    return markup


@bot.callback_query_handler(func=lambda call: call.data.startswith('menu1_'))
def callback_first_menu(call):
    if call.data == "menu1_boss":
        boss(call)
    elif call.data == "menu1_partner_cb":
        bot.send_message(call.message.chat.id, da.partner_post)
    elif call.data == "menu1_adj_cb":
        bot.send_message(call.message.chat.id, da.adjustment_of_work)
    elif call.data == "menu1_relation_with_agr":
        bot.send_message(call.message.chat.id, da.relations_with_agreement)
    elif call.data == "menu1_marketSMM_cb":
        bot.send_message(call.message.chat.id, da.marketing_and_SMM)
    elif call.data == "menu1_taxes_cb":
        bot.send_message(call.message.chat.id, da.nalog)
    elif call.data == "menu1_takeout_cb":
        bot.send_message(call.message.chat.id, da.takeout_from_PVZ)
    elif call.data == "menu1_coop_cb2":
        bot.send_message(call.message.chat.id, 'Раздел: Условия сотрудничества', reply_markup=coop())
    else:
        call.message.chat.id = "Не совсем понял, что было выбрано..."


@bot.message_handler(content_types=['text'])
def function_name(message):
    text = message.text.lower()
    to_bot_handler_list=['bot', 'бот', 'афанасий', 'нафаня']
    message_to_bot = any([True for _ in to_bot_handler_list if _ in text.split(" ")])
    print(message_to_bot)
    if True:

        q_greetings = ['ривет', 'еллоу', 'обрый день', 'авствуй']
        greetings_ans = ['Привет! Как жизнь молодая?', 'Готов помочь! Спрашивайте!',
                         'Добрый день! Готов помочь :)', 'Рад Вас видеть!',
                         'Добрый день!', 'Хеллоу :)']
        end_talk = ['Пока не знаю, как на это ответить (:', 'Прикинь, я макароны умею варить. Будешь со мной макароны?',
                    'Нам есть о чем побеседовать.', 'Прикольно. Но непонятно.', 'Как-то это странно прозвучало...']
        q_anketa = ['оглас', 'анкет']
        if sum([1 for _ in q_greetings if _ in text]) >= 1:
            r = random.randint(0, len(greetings_ans) - 1)
            bot.send_message(message.chat.id, greetings_ans[r])
        elif sum([1 for _ in q_anketa if _ in text]) >= 2:
            bot.send_message(message.chat.id, "Вопрос по согласованию анкеты. "
                                              "На самом деле анкета либо есть, либо нет.")
        elif sum([1 for _ in ['что ты можешь', 'что ты умеешь', '_!', 'меню'] if _ in text]) == 1:
            bot.send_message(message.chat.id, "Если что, вот меню: ", reply_markup=welcome_func())
        else:
            r = random.randint(0, len(end_talk) - 1)
            bot.send_message(message.chat.id, end_talk[r])


# bot.send_message(message.chat.id, message.text)


print("бот запущен!")

bot.polling()
