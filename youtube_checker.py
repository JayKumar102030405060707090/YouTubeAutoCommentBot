import requests
import time
from config import YOUTUBE_API_KEY, CHANNEL_ID

def get_latest_video():
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url).json()
    if "items" in response:
        video_id = response["items"][0]["id"].get("videoId")
        return video_id
    return None
