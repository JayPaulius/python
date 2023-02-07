
import telebot
import random

bot = telebot.TeleBot('TOKEN')
print('server start')

class Sum:
    def number1(message):
        message = bot.send_message(message.chat.id, 'Введите число 1:')
        bot.register_next_step_handler(message, Sum.number2)
    def number2(message):
        try:
            num1 = int(message.text)
            message = bot.send_message(message.chat.id, 'Введите число 2:')
            bot.register_next_step_handler(message, Sum.result, num1)
        except Exception as e:
            bot.reply_to(message, 'oooops')
    def result(message, num1):
        try:
            num2 = int(message.text)
            bot.send_message(message.chat.id, f'{num1} + {num2} = {num1+num2}')
        except Exception as e:
            bot.reply_to(message, 'oooops')

class Candies:
    def candies_input(message):
        message = bot.send_message(message.chat.id, 'Введите общее количество конфет:')
        bot.register_next_step_handler(message, Candies.max_input)
    def max_input(message):
        global candies
        candies = int(message.text)
        message = bot.send_message(message.chat.id, 'Введите максимальное количество конфет за ход:')
        bot.register_next_step_handler(message, Candies.result)
    def result(message):
        global max
        max = int(message.text)
        game(message)

class Player:
    @bot.message_handler(content_types=['text'])
    def player_input(message):
        message = bot.send_message(message.chat.id, 'игрок:')
        bot.register_next_step_handler(message, Player.result)
    def result(message):
        global player_candy
        player_candy = int(message.text)

def game(message):
    global candies
    global max
    global player_candy
    player_candy = 0
    Player()
    while player_candy > max or player_candy < 0:
        bot.send_message(message.chat.id, f'за один ход можно забрать от 0 до {max} конфет')
        Player()
    candies -= player_candy
    bot.send_message(message.chat.id, f'конфет осталось: {candies}')
    bot_candy = random.randrange(1, max+1)
    bot.send_message(message.chat.id, f'бот: {bot_candy}')
    candies -= bot_candy
    bot.send_message(message.chat.id, f'конфет осталось: {candies}')
    while candies > 0:
        Player()
        while player_candy > max or player_candy < 0:
            bot.send_message(message.chat.id, f'за один ход можно забрать от 0 до {max} конфет')
            Player()
        candies -= player_candy
        if candies == 0:
            bot.send_message(message.chat.id, 'игрок победил')
            break
        bot.send_message(message.chat.id, f'конфет осталось: {candies}')
        bot_candy = random.randrange(1, max+1)
        bot.send_message(message.chat.id, f'бот: {bot_candy}')
        candies -= bot_candy
        bot.send_message(message.chat.id, f'конфет осталось: {candies}')

@bot.message_handler(commands=['help', 'start'])
def help(message):
    bot.send_message(message.chat.id, 
'''
/help - инфо
/sum - вычислить сумму двух чисел
/delete_words - удалить из текста все слова, содержащие "абв"
/game
''')

@bot.message_handler(commands=['sum'])
def start(message):
    Sum.number1(message)

@bot.message_handler(commands=['delete_words'])
def start(message):
    message = bot.send_message(message.chat.id, 'Введите текст:')
    bot.register_next_step_handler(message, delete_words)
def delete_words(message):
    bot.send_message(message.chat.id, ' '.join(list(filter(lambda el: 'абв' not in el, message.text.split()))))

@bot.message_handler(commands=['game'])
def print(message):
    Candies.candies_input(message)

bot.polling()

