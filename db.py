import datetime

from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = 27017

client = MongoClient(DB_HOST, DB_PORT)
DB = client['traffic-watcher']
IPS = DB['ips']
PROTOCOLS = DB['traffic']
HOSTS = DB['hosts']


def check_if_ip_exists(ip):
    return bool(IPS.find_one({'ip': ip}))


def check_if_protocol_exists(protocol):
    return bool(PROTOCOLS.find_one({'protocol': protocol}))


def check_if_mac_exists(mac):
    return bool(HOSTS.find_one({'mac': mac}))


def add_ip_to_db(ip, isDanger):
    IPS.insert_one({
        'ip': ip,
        'isDanger': isDanger,
        'hits': 1
    })


def add_protocol_to_db(protocol):
    PROTOCOLS.insert_one({
        'protocol': protocol,
        'hits': 1
    })


def add_mac_to_db(mac):
    HOSTS.insert_one({
        'mac': mac,
        'isBlocked': False,
        'isConnected': True,
        'lastConnected': datetime.datetime.now()
    })


def increase_ip_hits_count(ip):
    IPS.update_one({'ip': ip}, {'$inc': {'hits': 1}})


def increase_protocol_hits_count(protocol):
    PROTOCOLS.update_one({'protocol': protocol}, {'$inc': {'hits': 1}})


def change_connection_status(mac, isConnected):
    if isConnected:
        HOSTS.update_one({'mac': mac}, {'isConnected': True, 'lastConnected': datetime.datetime.now()})
    else:
        HOSTS.update_one({'mac': mac}, {'isConnected': False, 'lastConnected': '-'})



