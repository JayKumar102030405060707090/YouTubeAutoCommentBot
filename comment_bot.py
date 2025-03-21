import requests
from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, COMMENT_TEXT

def post_comment(video_id, access_token):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    
    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": COMMENT_TEXT
                    }
                }
            }
        }
    )
    response = request.execute()
    return response
