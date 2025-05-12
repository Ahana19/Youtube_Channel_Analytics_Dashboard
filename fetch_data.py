import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def get_channel_videos(channel_id):
    base_url = "https://www.googleapis.com/youtube/v3/"
    videos = []
    url = f"{base_url}search?key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20"
    res = requests.get(url).json()
    
    for item in res.get("items", []):
        if item["id"]["kind"] == "youtube#video":
            videos.append({
                "video_id": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "published_at": item["snippet"]["publishedAt"]
            })
    return videos

if __name__ == "__main__":
    data = get_channel_videos(CHANNEL_ID)
    print(data)
