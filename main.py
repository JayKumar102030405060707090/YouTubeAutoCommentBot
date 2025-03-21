import time
from youtube_checker import get_latest_video
from comment_bot import post_comment

def main():
    last_video = None
    while True:
        video_id = get_latest_video()
        if video_id and video_id != last_video:
            print(f"New video found: {video_id}, posting comment...")
            post_comment(video_id)
            last_video = video_id
        time.sleep(5)

if __name__ == "__main__":
    main()
