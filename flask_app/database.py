from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_URI = os.getenv('MONGODB_URI')

uri = MONGODB_URI
print(uri)
def connect():
    
    client = MongoClient(uri)
    
    try:
        client.admin.command("ping")
        print("Connected successfully")
        

    except Exception as e:
        print(e)
        raise Exception(
            "The following error occurred: ", e)

    db = client.test
    
    return db

