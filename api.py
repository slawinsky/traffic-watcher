import requests

URL = 'https://api.ipapi.is/'


def send_request(endpoint):
    try:
        url = URL + endpoint
        response = requests.get(url)
        return response
    except Exception:
        Exception('Could not send request to API')


def get_ip_address_report(ip):
    endpoint = '?q=' + ip
    return send_request(endpoint)
