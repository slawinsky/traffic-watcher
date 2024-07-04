from api import get_ip_address_report
import json


def get_ip_analyses(ip):
    report = get_ip_address_report(ip)
    data = json.loads(report.text)
    return data


def analyze_ip(ip):
    is_danger = False
    data = get_ip_analyses(ip)

    is_bogon = data['is_bogon']
    is_crawler = data['is_crawler']
    is_tor = data['is_tor']
    is_abuser = data['is_abuser']

    if is_bogon or is_crawler or is_tor or is_abuser:
        is_danger = True

    return is_danger