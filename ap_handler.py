from db import check_if_mac_exists, add_mac_to_db, change_connection_status
def handle_ap_connection(mac):
    if not check_if_mac_exists(mac):
        add_mac_to_db(mac)
    else:
        change_connection_status(mac, True)


def handle_ap_disconnection(mac):
    change_connection_status(mac, False)

