import import_data
import export_data

choice = '''Выберите режим работы: 
1 - добавить группу
2 - добавить студента
3 - редактировать студента
4 - удалить студента
5 - вывести данные
6 - экспортировать в csv
0 - выход из программы
'''

def user_choice():
    user_input = input(choice)
    if user_input == '0':
        return 0
    elif user_input == '1':
        import_data.create_group()
        user_choice()
    elif user_input == '2':
        import_data.create_student()
        user_choice()
    elif user_input == '3':
        import_data.edit_student()
        user_choice()
    elif user_input == '4':
        import_data.delete_student()
        user_choice()
    elif user_input == '5':
        export_data.print_info()
        user_choice()
    elif user_input == '6':
        export_data.export_csv()
        user_choice()
    else:
        print('Введно некорректное значение')
        user_choice()