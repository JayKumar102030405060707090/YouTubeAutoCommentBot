import requests
import json
import time
from config import YOUTUBE_API_KEY, COMMENT_TEXT

def post_comment(video_id):
    """YouTube वीडियो पर कमेंट पोस्ट करना"""
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&key={YOUTUBE_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "snippet": {
            "videoId": video_id,
            "topLevelComment": {
                "snippet": {
                    "textOriginal": COMMENT_TEXT
                }
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"✅ कमेंट पोस्ट किया गया: {video_id}")
    else:
        print(f"❌ कमेंट फेल हुआ: {response.text}")

if __name__ == "__main__":
    while True:
        try:
            with open("latest_video.txt", "r") as f:
                latest_video_id = f.read().strip()
                post_comment(latest_video_id)
        except FileNotFoundError:
            print("⚠️ अभी तक कोई नया वीडियो नहीं मिला!")
        
        time.sleep(0.5)  # 0.5 सेकंड में एक बार चेक करना
