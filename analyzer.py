from api import get_ip_address_report
import json


def get_ip_analyses(ip):
    report = get_ip_address_report(ip)
    data = json.loads(report.text)
    analyses = data['data']['attributes']['last_analysis_results']
    return analyses


def analyze_ip(ip):
    is_danger = False
    analyses = get_ip_analyses(ip)

    for analysis in analyses:
        result = analyses[analysis]['result']
        if result == 'malicious' or result == 'malware':
            is_danger = True
            break

    return is_danger
