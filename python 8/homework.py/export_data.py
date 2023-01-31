def print_info():
    choice = 'Выберите данные для вывода:\n1 - список студентов\n2 - список групп\n0 - назад\n'
    user_input = input(choice)
    while user_input != '0':
        if user_input == '1':
            with open('students.txt', 'r', encoding='utf-8') as data:
                print(data.read())
            user_input = input(choice)
        elif user_input == '2':
            with open('groups.txt', 'r', encoding='utf-8') as data:
                print(data.read())
            user_input = input(choice)

def export_csv():
    with open('students.txt', 'r', encoding='utf-8') as data:
        lines = data.read()
    with open('students.csv', 'w', encoding='utf-8') as data:
        data.write(lines)
    print('Данные экспортированы')