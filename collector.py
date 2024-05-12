from db import check_if_ip_exists, check_if_protocol_exists, add_ip_to_db, add_protocol_to_db, increase_ip_hits_count, increase_protocol_hits_count
from analyzer import analyze_ip
from ebtables import block_ip_address
from exceptions import exceptions


def collect_ip(ip):
    if not check_if_ip_exists(ip) and ip not in exceptions:
        isDanger = analyze_ip(ip)
        if isDanger:
            block_ip_address(ip)
        add_ip_to_db(ip, isDanger)
    else:
        increase_ip_hits_count(ip)


def collect_protocol(protocol):
    if not check_if_protocol_exists(protocol):
        add_protocol_to_db(protocol)
    else:
        increase_protocol_hits_count(protocol)

