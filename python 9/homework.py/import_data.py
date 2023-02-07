def add_data(name, tel, info):
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        file.write(f'{name}; {tel}; {info} \n')
