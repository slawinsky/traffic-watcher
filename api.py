from dotenv import load_dotenv
import requests

load_dotenv()
URL = 'https://api.ipapi.is/'


def send_request(endpoint):
    url = URL + endpoint
    response = requests.get(url)
    return response


def get_ip_address_report(ip):
    endpoint = '?q=' + ip
    return send_request(endpoint)

