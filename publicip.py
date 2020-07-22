import requests
import json

def get_ip_info():
    response = requests.get('https://ifconfig.co/json')
    public_ip_info = json.loads(response.content.decode('utf-8'))
    return (public_ip_info['ip'], public_ip_info['region_name'], public_ip_info['asn_org'])
