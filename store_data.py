from pymongo import MongoClient
from fetch_data import get_channel_videos
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client.youtube_analytics
collection = db.videos

data = get_channel_videos(os.getenv("CHANNEL_ID"))

if data:
    collection.insert_many(data)
    print("Data stored successfully")
else:
    print("No data found")
