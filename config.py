import os
from dotenv import load_dotenv

# .env फाइल से API Keys लोड करना
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")  # YouTube API Key
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Telegram Bot का Token
CHANNEL_ID = os.getenv("CHANNEL_ID")  # YouTube चैनल ID जिसपर नजर रखनी है
COMMENT_TEXT = os.getenv("COMMENT_TEXT")  # जो कमेंट करना है
