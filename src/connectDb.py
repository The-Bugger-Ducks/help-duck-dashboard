from pymongo import MongoClient

def connect():
  db = MongoClient("mongodb+srv://<user>:<password>@helpduck.v3mv8.mongodb.net")
  return db['test']

