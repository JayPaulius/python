from user_interface import get_data, print_data
from model_calc import calculate
import logger

def run():
    a = get_data('variable1')
    logger.data_logger(a, 'variable1')
    b = get_data('variable2')
    logger.data_logger(b, 'variable2')
    op = get_data('operator')
    logger.data_logger(op, 'operator')
    result = calculate(a, b, op)
    logger.data_logger(result, 'result')
    print_data(result)