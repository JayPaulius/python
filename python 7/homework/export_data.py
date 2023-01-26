def print_phonebook():
    with open('phonebook.csv', 'r', encoding="utf-8") as data:
        print(data.read())