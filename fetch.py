from pymongo import MongoClient
import sys, os
from dotenv import load_dotenv
load_dotenv()

license_number = sys.argv[1] #LICENSE_NUMBER

mongodblink = os.environ['DB_URL']

cluster = MongoClient(mongodblink)
collection = cluster['user-data']

users = collection['customers']

for user in users.find({"license":f"{license_number}"}):
    print(f"{user['name']}\t{user['license']}")
