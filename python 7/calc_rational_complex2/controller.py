from model_calc import calculate
from user_interface import get_data
from logger import data_logger

def get_controller():
    data_logger('', 'старт')
    return calculate(*get_data())