from db import check_if_ip_exists, add_to_db, increase_hits_count
from analyzer import analyze_ip
from ebtables import block_ip_address
from exceptions import exceptions


def collect_ip(ip):
    if not check_if_ip_exists(ip) and ip not in exceptions:
        isDanger = analyze_ip(ip)
        if isDanger:
            block_ip_address(ip)
        add_to_db(ip, isDanger)
    else:
        increase_hits_count(ip)

