import re
import time

FILE_PATH = "/var/log/traffic.log"
def find_ip_addresses(FILE_PATH):
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    with open(FILE_PATH, 'r') as file:
        for line in file:
            ip_addresses = re.findall(ip_regex, line)
            for ip in ip_addresses:
                print("Found IP address:", ip)

def monitor_file(FILE_PATH):
    while True:
        with open(FILE_PATH, 'r') as file:
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    break
                print("New line detected:", line.strip())
                find_ip_addresses(FILE_PATH)
        time.sleep(1)
