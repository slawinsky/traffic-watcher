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


def check_if_ip_exists(ip):
    return bool(IPS.find_one({'ip': ip}))


def check_if_protocol_exists(protocol):
    return bool(PROTOCOLS.find_one({'protocol': protocol}))


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


def increase_ip_hits_count(ip):
    IPS.update_one({'ip': ip}, {'$inc': {'hits': 1}})


def increase_protocol_hits_count(protocol):
    PROTOCOLS.update_one({'protocol': protocol}, {'$inc': {'hits': 1}})
