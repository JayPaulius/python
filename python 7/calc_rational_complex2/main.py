from controller import get_controller
from logger import print_log

user_input = int(input('Вычисление - 1. Вывод лога - 2: '))
while user_input < 1 or user_input > 2:
    user_input = int(input('Вычисление - 1. Вывод лога - 2: '))
if user_input == 1:
    print(get_controller())
else:
    print_log()