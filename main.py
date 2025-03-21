import threading
import youtube_checker
import comment_bot

def start_youtube_checker():
    youtube_checker.main()

def start_comment_bot():
    comment_bot.main()

if __name__ == "__main__":
    threading.Thread(target=start_youtube_checker).start()
    threading.Thread(target=start_comment_bot).start()
