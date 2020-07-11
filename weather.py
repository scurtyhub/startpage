import requests
from config import config_file_check
from common import get_config, USER_CONFIG_PATH


def get_current_weather():
    config = get_config(USER_CONFIG_PATH)
    app_id = config['DEFAULT'].get('weather_api_key', None)
    location = config['DEFAULT'].get('weather_location', 'Los Angeles')
    units = config['DEFAULT'].get('weather_units', 'metric')
    default_value = config['DEFAULT'].get('default_value', '-1')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location},US&units={units}&appid={app_id}'

    response = requests.get(url).json()

    return {
        'location': location,
        'description': response.get('weather', [{}])[0].get('description', -1),
        'temperature': {
            'now': response.get('main', {}).get('temp', default_value)
        }
    }
