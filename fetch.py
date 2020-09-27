from pymongo import MongoClient
import sys, os
from dotenv import load_dotenv
load_dotenv()

license_number = sys.argv[1] #LICENSE_NUMBER

pwd = os.environ['PASS']
customers = os.environ['COLLECTION']

mongodblink = f"mongodb+srv://admin:{pwd}@user-data.5mz9v.mongodb.net/{customers}?retryWrites=true&w=majority"

cluster = MongoClient(mongodblink)
collection = cluster['user-data']

users = collection[customers]

for user in users.find({"license":f"{license_number}"}):
    print(f"{user['name']} {user['license']}")
