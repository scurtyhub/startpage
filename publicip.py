import requests
import json

def get_ip_info():
    response = requests.get('https://ipinfo.io')
    public_ip_info = json.loads(response.content.decode('utf-8'))
    return (public_ip_info['ip'], public_ip_info['region'], public_ip_info['org'])
