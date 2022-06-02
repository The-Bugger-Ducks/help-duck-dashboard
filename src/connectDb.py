import os
from pymongo import MongoClient

def connect():
  db = MongoClient(f'mongodb+srv://{os.environ.get("MONGO_USERNAME")}:{os.environ.get("MONGO_PASSWORD")}@helpduck.v3mv8.mongodb.net')
  return db['db-help-duck']

