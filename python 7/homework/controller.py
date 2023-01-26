from user_interface import get_data
import import_data
import export_data

def get_controller(mode):
    if mode == 1:
        import_data.add_data_format_1(*get_data())
    else:
        import_data.add_data_format_2(*get_data())

def print_data(mode):
    if mode == 1:
        export_data.print_phonebook_format_1()
    else:
        export_data.print_phonebook_format_2()