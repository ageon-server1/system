from pymongo import MongoClient
from bot_config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['gpt_bot']
