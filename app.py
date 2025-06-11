import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()


mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)
import pymongo