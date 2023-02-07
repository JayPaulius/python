# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import telebot
from logger import data_logger
from calc import calculate
import import_data
bot = telebot.TeleBot('TOKEN')
print('server start')



def check_data(data):
    if 'j' in data:
        data = data.replace(" ", "")
        data = complex(data)
    else:
        data = float(data)
    return data

def export_1(message):
    with open('phonebook.csv', 'r', encoding="utf-8") as data:
        bot.send_message(message.chat.id, data.read())

def export_2(message):
    document = open('phonebook.csv', 'r', encoding="utf-8")
    bot.send_document(message.chat.id, document)

@bot.message_handler(commands=['help', 'start'])
def help(message):
    bot.send_message(message.chat.id, 
'''
/help - инфо
/calc - калькулятор для работы с рациональными и комплексными числами
/tel - телефонный справочник
''')

@bot.message_handler(commands=['calc'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Введите рациональное число или комплексное число в формате x+yj:')
    bot.register_next_step_handler(msg, num1)
def num1(message):
    num1 = message.text
    num1 = check_data(num1)
    data_logger(message.chat.id, 'id')
    data_logger(num1, 'number_1')
    msg = bot.send_message(message.chat.id, 'Ведите рациональное число или комплексное число в формате x+yj:')
    bot.register_next_step_handler(msg, num2, num1)
def num2(message, num1):
    num2 = message.text
    num2 = check_data(num2)
    data_logger(num2, 'number_2')
    msg = bot.send_message(message.chat.id, 'Введите оператор:')
    bot.register_next_step_handler(msg, op, num1, num2)
def op(message, num1, num2):
    op = message.text
    data_logger(op, 'operator')
    result = calculate(num1, num2, op)
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['tel'])
def start(message):
    msg = bot.send_message(message.chat.id, 
'''Выберите режим работы:
1 - добавить данные в телефонную книгу
2 - вывести телефонную книгу на экран
3 - экспортировать телефонную книгу в csv файл''')
    bot.register_next_step_handler(msg, mode)
def mode(message):
    mode = int(message.text)
    if mode == 2:
        export_1(message)
    elif mode == 3:
        export_2(message)
    else:
        msg = bot.send_message(message.chat.id, 'Введите имя:')
        bot.register_next_step_handler(msg, name)
def name(message):
    name = message.text
    msg = bot.send_message(message.chat.id, 'Введите телефон:')
    bot.register_next_step_handler(msg, tel, name)
def tel(message, name):
    tel = message.text
    msg = bot.send_message(message.chat.id, 'Введите описание:')
    bot.register_next_step_handler(msg, info, name, tel)
def info(message, name, tel):
    info = message.text
    import_data.add_data(name, tel, info)
    bot.send_message(message.chat.id, 'данные успешно сохранены')

bot.polling()
