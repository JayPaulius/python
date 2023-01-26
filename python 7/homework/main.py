from controller import get_controller
from export_data import print_phonebook

user_input = int(input('Выберите режим работы: \n 1 - добавить данные в телефонную книгу \n 2 - вывести телефонную книгу на экран \n'))
while user_input < 1 or user_input > 2:
    user_input = int(input('Выберите режим работы: \n 1 - добавить данные в телефонную книгу \n 2 - вывести телефонную книгу на экран \n'))
if user_input == 1:
    user_input = int(input('Выберите формат данных: \n 1 - добавить данные в одну строку \n 2 - добавить данные в несколько строк \n'))
    while user_input < 1 or user_input > 2:
        user_input = int(input('Выберите формат данных: \n 1 - добавить данные в одну строку \n 2 - добавить данные в несколько строк \n'))
    get_controller(user_input)
else:
    print_phonebook()