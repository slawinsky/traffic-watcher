import re
import time
from collector import collect_ip, collect_protocol


def find_ip_addresses(line):
    ip_regex = r'\b(?!192\.168\.33\.\d{1,3}\b)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ip_addresses = re.findall(ip_regex, line)
    for ip in ip_addresses:
        collect_ip(ip)


def find_protocols(line):
    protocol_regex = r'proto=(\d+)'
    protocols = re.findall(protocol_regex, line)
    for protocol in protocols:
        collect_protocol(protocol)


def monitor_file(path):
    file = open(path)
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        find_ip_addresses(line.strip())
        find_protocols(line.strip())