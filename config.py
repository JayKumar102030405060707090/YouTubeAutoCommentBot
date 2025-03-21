import os
from dotenv import load_dotenv

# .env फाइल से API Keys लोड करना
load_dotenv()

YOUTUBE_API_KEY = os.getenv("AIzaSyAOorokSXnBGeDFte5_LoxXWh6MYPIOq7I")  # YouTube API Key
TELEGRAM_BOT_TOKEN = os.getenv("7605033751:AAFAkK096F2N65qS5pMDGEQfP8FzN5rxtIY")  # Telegram Bot का Token
CHANNEL_ID = os.getenv("UCY5QxBSs6MVM1OOOAG9I2LQ")  # YouTube चैनल ID जिसपर नजर रखनी है
COMMENT_TEXT = os.getenv("My first comment i am winner")  # जो कमेंट करना है
