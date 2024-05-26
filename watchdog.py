import re
import time
from collector import collect_ip, collect_protocol
from ap_handler import handle_ap_connection, handle_ap_disconnection


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


def find_ap_events(line):
    handshake_regex = r'\b([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})\b(?=.*handshake completed)'
    mac_addresses = re.findall(handshake_regex, line)
    for mac in mac_addresses:
        handle_ap_connection(mac)

    disassociation_regex = r'\b([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})\b(?=.*disassociated)'
    mac_addresses = re.findall(disassociation_regex, line)
    for mac in mac_addresses:
        handle_ap_disconnection(mac)


def monitor_file(path):
    traffic = open(path)
    traffic.seek(0, 2)
    while True:
        traffic_line = traffic.readline()
        if not traffic_line:
            time.sleep(0.1)
            continue
        find_ip_addresses(traffic_line.strip())
        find_protocols(traffic_line.strip())
        find_ap_events(traffic_line.strip())