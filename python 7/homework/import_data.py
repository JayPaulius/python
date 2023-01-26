def add_data_format_1(first_name, last_name, tel, info):
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        file.write('\n')
        file.write(f'{first_name}; {last_name}; {tel}; {info} \n')
    print('данные успешно сохранены в файле phonebook.csv')

def add_data_format_2(first_name, last_name, tel, info):
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        file.write('\n')
        file.write(f'{first_name}\n')
        file.write(f'{last_name}\n')
        file.write(f'{tel}\n')
        file.write(f'{info}\n')
    print('данные успешно сохранены в файле phonebook.csv')