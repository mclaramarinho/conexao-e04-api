from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ

load_dotenv()

client = MongoClient(environ["ATLAS_URI"])
db = client.get_database(environ["DB_NAME"])

