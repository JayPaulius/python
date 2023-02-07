from logger import data_logger

def calculate(x, y, operator):
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        result = x / y
    data_logger(result, 'result')
    return result
