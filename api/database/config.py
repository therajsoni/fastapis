from pymongo import MongoClient
from dotenv import load_dotenv 
import os 

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
Client = MongoClient(MONGO_URL)
Database = Client["BookApp"]
books = Database["books"]
users = Database["users"]

