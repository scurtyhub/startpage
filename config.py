import configparser
import os
from common import get_config


USER_CONFIG_PATH = os.path.expanduser('config.ini')


def config_file_check():
    try:
        config = get_config(USER_CONFIG_PATH) 
        if not (config['DEFAULT']['weather_location'] and config['DEFAULT']['weather_api_key'] and config['DEFAULT']['weather_units']):
            return False
        return config['DEFAULT']['weather_location'], config['DEFAULT']['weather_api_key'], config['DEFAULT']['weather_units']
    except KeyError:
        return False
