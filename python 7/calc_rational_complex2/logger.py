from datetime import datetime as dt

def data_logger(data, title):
    time = dt.now().strftime('%H:%M:%S')
    with open('log.csv', 'a', encoding="utf-8") as file:
        file.write(f'{time}; {title}; {data}\n')

def print_log():
    with open('log.csv', 'r', encoding="utf-8") as data:
        print(data.read())