import os
import configparser


USER_CONFIG_PATH = os.getcwd() + '/config.ini'

def file_exists(file_path):
    return True if os.path.isfile(file_path) else False


def read_file(file_path):
    if not file_exists(file_path):
        return []
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines


def get_config(file_path):
    if not file_exists:
        return False
        # raise exception
    config = configparser.ConfigParser()
    config.read(file_path)
    return config
    