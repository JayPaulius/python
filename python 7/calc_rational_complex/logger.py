from datetime import datetime as dt

def data_logger(data, title):
    time = dt.now().strftime('%H:%M:%S')
    with open('log.csv', 'a') as file:
        file.write(f'{time}; {title}; {data}\n')
