def get_data(title):
    if title != 'operator':
        print('Введите рациональное число или комплексное число в формате x+yj:')
        data = input()
        data = check_type(data)
    else:
        print('Введите оператор:')
        data = input()
    return data

def check_type(data):
    if 'j' in data:
        data = data.replace(" ", "")
        data = complex(data)
    else:
        data = float(data)
    return data

def print_data(data):
    print(f'result = {data}')