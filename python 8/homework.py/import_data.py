def check_element(element, data):
    for el in data:
        list1 = el.split('; ')
        if list1[0] == element:
            return 1

def create_group():
    group = input('Введите группу: ')
    with open('groups.txt', 'r+', encoding='utf-8') as data:
        while check_element(group, data) == 1:
            data.seek(0)
            group = input('Такая группа уже существует. Введите другую группу или введите 0 для выхода: ')
            if group == '0':
                return 0
        data.write(f'{group}; 0\n')
        print('Группа добавлена')

def select_group(old_group):
    with open('groups.txt', 'r', encoding='utf-8') as data:
        print('Выберите группу из списка: ')
        for el in data:
            list1 = el.split('; ')
            print(list1[0])
        group = input()
        data.seek(0)
        while check_element(group, data) != 1:
            data.seek(0)
            group = input('Такой группы не существует. Выберите группу из списка или введите 0 и выберите пункт "добавить группу": ')
            if group == '0':
                return 0
        increment_students_count(group)
        if old_group != 0:
            if '\n' in old_group:
                old_group = old_group[:-1]
            decrement_students_count(old_group)
        return group

def select_id():
    with open('students.txt', 'r', encoding='utf-8') as data:
        print('Выберите id студента, которого хотите отредактировать: ')
        print(data.read())
        id_num = input()
        data.seek(0)
        while check_element(id_num, data) != 1:
            data.seek(0)
            id_num = input('Такого id не существует. Выберите id из списка или введите 0 для выхода: ')
            if id_num == '0':
                return 0
        return id_num

def increment_students_count(group):
    with open('groups.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, el in enumerate(data):
        list1 = el.split('; ')
        if list1[0] == group:
            list1[1] = str(int(list1[1]) + 1)
            id_num = i
            break
    data[int(id_num)] = "; ".join(list1) + '\n'
    with open('groups.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

def decrement_students_count(group):
    with open('groups.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, el in enumerate(data):
        list1 = el.split('; ')
        if list1[0] == group:
            list1[1] = str(int(list1[1]) - 1)
            id_num = i
            break
    data[int(id_num)] = "; ".join(list1) + '\n'
    with open('groups.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

def create_student():
    firstname = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    birthdate = input('Введите дату рождения: ')
    tel = input('Введите телефон: ')
    id_num = ''
    group = select_group(0)
    if group == 0:
        return 0
    with open('students.txt', 'r+', encoding='utf-8') as data:
        for el in data:
            list1 = el.split('; ')
            id_num = list1[0]
        id_num = int(id_num)
        data.write(f'{id_num + 1}; {firstname}; {lastname}; {birthdate}; {tel}; {group}\n')
        print('Студент добавлен')

def edit_student():
    list2 = []
    id_num = select_id()
    if id_num == 0:
        return 0
    with open('students.txt', 'r', encoding='utf-8') as data:
        for el in data:
            list1 = el.split('; ')
            if id_num == list1[0]:
                list2 = list1[:]
                break
    print(list1)
    choice = 'Выберите данные для редактирования:\n1 - имя\n2 - фамилия\n3 - дата рождения\n4 - телефон\n5 - группа\n0 - сохранить и выйти\n'
    user_input = input(choice)
    while user_input != '0':
        if user_input == '1':
            list2[1] = input('Введите имя: ')
            print(list2)
            user_input = input(choice)
        elif user_input == '2':
            list2[2] = input('Введите фамилию: ')
            print(list2)
            user_input = input(choice)
        elif user_input == '3':
            list2[3] = input('Введите дату рождения: ')
            print(list2)
            user_input = input(choice)
        elif user_input == '4':
            list2[4] = input('Введите телефон: ')
            print(list2)
            user_input = input(choice)
        elif user_input == '5':
            list2[5] = select_group(list2[5])
            print(list2)
            user_input = input(choice)
        else:
            print('Введно некорректное значение')
            user_input = input(choice)
    if list2 != list1:
        with open('students.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        data[int(id_num)] = "; ".join(list2) + '\n'
        with open('students.txt', 'w', encoding='utf-8') as file:
            for line in data:
                if not line.isspace():
                    file.write(line)

def delete_student():
    print('Выберите id студента, которого хотите удалить: ')
    with open('students.txt', 'r', encoding='utf-8') as data:
        print(data.read())
        id_num = input()
        data.seek(0)
        while check_element(id_num, data) != 1:
            data.seek(0)
            id_num = input('Такого id не существует. Выберите id из списка или введите 0 для выхода: ')
            if id_num == '0':
                return 0
        data.seek(0)
        lines = data.readlines()
        with open('students.txt', 'w', encoding='utf-8') as data:
            for i, line in enumerate(lines):
                if i != int(id_num):
                    if i > int(id_num):
                        list1 = line.split('; ')
                        list1[0] = str(int(list1[0])-1)
                        line = "; ".join(list1)
                        data.write(line)
                    else:
                        data.write(line)
            print('Студент удален')