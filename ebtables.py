import os


def block_ip_address(ip):
    try:
        os.system(f'sudo ebtables -A FORWARD -p ivp4 -i wlan0 --ip-src {ip} -j DROP')
        os.system(f'sudo ebtables -A INPUT -p ivp4 -i wlan0 --ip-dst {ip} -j DROP')
    except Exception:
        print('Could not add ebtables rule')

