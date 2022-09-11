#systemctl start telebot_1

# v1.0.0 - изменение статических данных на динамически обновляемые
# v1.1.0 - изменение способа получения данных с сайта
# v1.1.1 - изменение ошибки в расписании звонков
# v1.2.0 - добавление логирования сообщений и ников пользователей


import telebot
import requests
import urllib.request
import random
import tg_analytic
import csv

from telebot import types
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

TOKEN = ""
ID_ADMIN = ""

bot = telebot.TeleBot(TOKEN)

HELP = """
БОТ "РАСПИСАНИЕ ИТ СИБГУТИ"
!РАСПИСАНИЕ ВЫВОДИТСЯ ТОЛЬКО ДЛЯ ИНСТИТУТА ТЕЛЕКОММУНИКАЦИЙ!

/help - вывести список доступных команд
/groups - вывести список групп
/calls - вывести расписание звонков

Бот постоянно обновляется.
Вопросы и предложения автору ⚙️
@lc_local

v1.2.0
 """

CALLS = """
1️⃣ 8:00-9:35
💩15 минут💩
2️⃣ 9:50-11:25
💩15 минут💩
3️⃣ 11:40-13:15
💩30 минут💩
4️⃣ 13:45-15:20
💩15 минут💩
5️⃣ 15:35-17:10
💩15 минут💩
6️⃣ 17:25-19:00
"""

LINK = "https://sibsutis.ru/students/study/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BE%D1%87%D0%BD%D0%BE%D0%B9%20%D1%84%D0%BE%D1%80%D0%BC%D1%8B%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F/2022-2023%20%D1%83%D1%87.%D0%B3%D0%BE%D0%B4/I%20%D0%BF%D0%BE%D0%BB%D1%83%D0%B3%D0%BE%D0%B4%D0%B8%D0%B5%202022-2023%20%D1%83%D1%87.%D0%B3%D0%BE%D0%B4_/%D0%98%D0%A2/1%20%D0%BA%D1%83%D1%80%D1%81"

list_link = []
list_name = []
list_size = []
list_owner = []
list_datemodify = []

@bot.message_handler(commands=["database"])
def answer(message):
    if (message.from_user.id == ID_ADMIN):
        bot.send_document(ID_ADMIN, document=open('/home/lev/bot_schedule/data.csv'))

@bot.message_handler(commands=['groups'])
def groups(message):
    tg_analytic.statistics(message.from_user.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(list_name[0].replace('.docx', ''))
    btn2 = types.KeyboardButton(list_name[1].replace('.docx', ''))
    btn3 = types.KeyboardButton(list_name[2].replace('.docx', ''))
    btn4 = types.KeyboardButton(list_name[3].replace('.docx', ''))
    btn5 = types.KeyboardButton(list_name[4].replace('.docx', ''))
    btn6 = types.KeyboardButton(list_name[5].replace('.docx', ''))
    btn7 = types.KeyboardButton(list_name[6].replace('.docx', ''))
    btn8 = types.KeyboardButton(list_name[7].replace('.docx', ''))
    btn9 = types.KeyboardButton(list_name[8].replace('.docx', ''))
    btn10 = types.KeyboardButton(list_name[9].replace('.docx', ''))
    btn11 = types.KeyboardButton(list_name[10].replace('.docx', ''))
    btn12 = types.KeyboardButton(list_name[11].replace('.docx', ''))
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    bot.send_message(message.chat.id, text="Ну привет, {0.first_name}! Добро пожаловать, сынок)0".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['calls'])
def calls(message):
    tg_analytic.statistics(message.from_user.id, message.text)
    bot.send_message(message.chat.id, text="👀")
    bot.send_message(message.chat.id, text=CALLS)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if (str(call.data) == list_name[0]):
        text = list_name[0].replace('.docx', '') + "\nАвтор: " + list_owner[0] + "\nРазмер: " + list_size[0] + "\nПоследнее изменение: " + list_datemodify[0]
        bot.answer_callback_query(call.id, show_alert=True, text=text)

    if (str(call.data) == list_name[1]):
        text = list_name[1].replace('.docx', '') + "\nАвтор: " + list_owner[1] + "\nРазмер: " + list_size[1] + "\nПоследнее изменение: " + list_datemodify[1]
        bot.answer_callback_query(call.id, show_alert=True, text=text)

    if (str(call.data) == list_name[2]):
        text = list_name[2].replace('.docx', '') + "\nАвтор: " + list_owner[2] + "\nРазмер: " + list_size[2] + "\nПоследнее изменение: " + list_datemodify[2]
        bot.answer_callback_query(call.id, show_alert=True, text=text)

    if (str(call.data) == list_name[3]):
        text = list_name[3].replace('.docx', '') + "\nАвтор: " + list_owner[3] + "\nРазмер: " + list_size[3] + "\nПоследнее изменение: " + list_datemodify[3]
        bot.answer_callback_query(call.id, show_alert=True, text=text)

    if (str(call.data) == list_name[4]):
        text = list_name[4].replace('.docx', '') + "\nАвтор: " + list_owner[4] + "\nРазмер: " + list_size[4] + "\nПоследнее изменение: " + list_datemodify[4]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[5]):
        text = list_name[5].replace('.docx', '') + "\nАвтор: " + list_owner[5] + "\nРазмер: " + list_size[5] + "\nПоследнее изменение: " + list_datemodify[5]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[6]):
        text = list_name[6].replace('.docx', '') + "\nАвтор: " + list_owner[6] + "\nРазмер: " + list_size[6] + "\nПоследнее изменение: " + list_datemodify[6]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[7]):
        text = list_name[7].replace('.docx', '') + "\nАвтор: " + list_owner[7] + "\nРазмер: " + list_size[7] + "\nПоследнее изменение: " + list_datemodify[7]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[8]):
        text = list_name[8].replace('.docx', '') + "\nАвтор: " + list_owner[8] + "\nРазмер: " + list_size[8] + "\nПоследнее изменение: " + list_datemodify[8]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[9]):
        text = list_name[9].replace('.docx', '') + "\nАвтор: " + list_owner[9] + "\nРазмер: " + list_size[9] + "\nПоследнее изменение: " + list_datemodify[9]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[10]):
        text = list_name[10].replace('.docx', '') + "\nАвтор: " + list_owner[10] + "\nРазмер: " + list_size[10] + "\nПоследнее изменение: " + list_datemodify[10]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    if (str(call.data) == list_name[11]):
        text = list_name[11].replace('.docx', '') + "\nАвтор: " + list_owner[11] + "\nРазмер: " + list_size[11] + "\nПоследнее изменение: " + list_datemodify[11]
        bot.answer_callback_query(call.id, show_alert=True, text=text)
    bot.answer_callback_query(call.id)


@bot.message_handler(content_types=['text'])
def func(message):
    tg_analytic.statistics(message.from_user.id, message.text)
    markup = types.InlineKeyboardMarkup()
    if(message.text == list_name[0].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[0]))
        bot.send_message(message.chat.id, text="Пожалуйста...")
        url_download = list_link[0]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[0], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[0], 'rb'), reply_markup=markup)

    elif(message.text == list_name[1].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[1]))
        bot.send_message(message.chat.id, text="Не нужно благодарности!")
        url_download = list_link[1]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[1], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[1], 'rb'), reply_markup=markup)

    elif(message.text == list_name[2].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[2]))
        bot.send_message(message.chat.id, text="Хочешь словить пердечный сриступ?")
        url_download = list_link[2]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[2], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[2], 'rb'), reply_markup=markup)

    elif(message.text == list_name[3].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[3]))
        bot.send_message(message.chat.id, text="Я не советую смотреть это...")
        url_download = list_link[3]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[3], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[3], 'rb'), reply_markup=markup)

    elif(message.text == list_name[4].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[4]))
        bot.send_message(message.chat.id, text="Беги...")
        url_download = list_link[4]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[4], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[4], 'rb'), reply_markup=markup)

    elif(message.text == list_name[5].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[5]))
        bot.send_message(message.chat.id, text="Ты прекрасна)")
        url_download = list_link[5]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[5], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[5], 'rb'), reply_markup=markup)

    elif(message.text == list_name[6].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[6]))
        bot.send_message(message.chat.id, text="Может не стоит?")
        url_download = list_link[6]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[6], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[6], 'rb'), reply_markup=markup)

    elif(message.text == list_name[7].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[7]))
        bot.send_message(message.chat.id, text="Ну давай посмотрим, что там")
        url_download = list_link[7]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[7], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[7], 'rb'), reply_markup=markup)

    elif(message.text == list_name[8].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[8]))
        bot.send_message(message.chat.id, text="Чекай пока горячее")
        url_download = list_link[8]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[8], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[8], 'rb'), reply_markup=markup)

    elif(message.text == list_name[9].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[9]))
        bot.send_message(message.chat.id, text="Помянем")
        url_download = list_link[9]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[9], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[9], 'rb'), reply_markup=markup)

    elif(message.text == list_name[10].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[10]))
        bot.send_message(message.chat.id, text="Спасибо тебе, что разбудил меня")
        url_download = list_link[10]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[10], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[10], 'rb'), reply_markup=markup)

    elif(message.text == list_name[11].replace('.docx', '')):
        markup.add(types.InlineKeyboardButton(text="Информация", callback_data=list_name[11]))
        bot.send_message(message.chat.id, text="Я устал")
        url_download = list_link[11]
        myfile = requests.get(url_download, verify=False)
        open('/home/lev/bot_schedule/schedule/' + list_name[11], 'wb').write(myfile.content)
        bot.send_document(message.chat.id, document=open('/home/lev/bot_schedule/schedule/' + list_name[11], 'rb'), reply_markup=markup)

    elif(message.text == "/help" or message.text == "/start"):
        bot.send_message(message.chat.id, HELP)
    else:
        bot.send_message(message.chat.id, text="Извинись...")


def main():
    link = LINK
    print(get_data(get_html(link)))

def get_html(link):
    response = requests.get(link, verify=False)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    # Парсинг данных с сайта и запись в соответствующие списки
    for a in soup.find_all('a', class_='element-title'):
        #print(a.get('data-bx-src'))
        list_link.append(a.get('data-bx-src'))
        list_name.append(a.text)
        list_size.append(a.get('data-bx-size'))
        list_owner.append(a.get('data-bx-owner'))
        list_datemodify.append(a.get('data-bx-datemodify'))

    for link in range(len(list_link)):
        list_link[link] = 'https://sibsutis.ru' + list_link[link]
    print(list_link)

if __name__ == '__main__':
    main()
    # Постоянное обращение к серверам телеграм
    bot.polling(none_stop=True)
