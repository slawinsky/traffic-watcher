from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = 27017

client = MongoClient(DB_HOST, DB_PORT)
DB = client['traffic-watcher']
IPS = DB['ips']


def check_if_ip_exists(ip):
    return bool(IPS.find_one({'ip': ip}))


def add_to_db(ip, isDanger):
    IPS.insert_one({
        'ip': ip,
        'isDanger': isDanger
    })




