from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv('VIRUSTOTAL_API_KEY')
URL = 'https://www.virustotal.com/api/v3/'
HEADERS = {
    'accept': 'application/json',
    'x-apikey': API_KEY
}


def send_request(endpoint):
    url = URL + endpoint
    response = requests.get(url, headers=HEADERS)
    return response


def get_ip_address_report(ip):
    endpoint = 'ip_addresses/' + ip
    return send_request(endpoint)

