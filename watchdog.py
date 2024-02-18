import re
import time

def find_ip_addresses(file_path):
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    with open(file_path, 'r') as file:
        for line in file:
            ip_addresses = re.findall(ip_regex, line)
            for ip in ip_addresses:
                print("Found IP address:", ip)

def monitor_file(file_path):
    while True:
        with open(file_path, 'r') as file:
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    break
                print("New line detected:", line.strip())
                find_ip_addresses(file_path)
        time.sleep(1)
