import requests
import time
from config import YOUTUBE_API_KEY, CHANNEL_ID

def get_latest_video():
    """YouTube चैनल से सबसे नया वीडियो ID निकाले"""
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url).json()
    
    if "items" in response:
        video_id = response["items"][0]["id"]["videoId"]
        return video_id
    return None

if __name__ == "__main__":
    latest_video = None

    while True:
        video_id = get_latest_video()
        
        if video_id and video_id != latest_video:
            print(f"🔔 नया वीडियो मिला: {video_id}")
            latest_video = video_id
            with open("latest_video.txt", "w") as f:
                f.write(video_id)  # नया वीडियो ID सेव करना

        time.sleep(0.5)  # हर 0.5 सेकंड बाद चेक करना
