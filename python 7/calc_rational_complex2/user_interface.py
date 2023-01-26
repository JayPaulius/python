from logger import data_logger

def get_data():
    a = input('Введите рациональное число или комплексное число в формате x+yj: ')
    a = check_data(a)
    data_logger(a, 'variable1')
    b = input('Введите рациональное число или комплексное число в формате x+yj: ')
    b = check_data(b)
    data_logger(b, 'variable2')
    op = input('Введите оператор: ')
    data_logger(op, 'operator')
    return a, b, op

def check_data(data):
    if 'j' in data:
        data = data.replace(" ", "")
        data = complex(data)
    else:
        data = float(data)
    return data
