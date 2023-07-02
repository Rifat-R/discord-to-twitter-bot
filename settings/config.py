import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
BOT_API_KEY = os.getenv("BOT_API_KEY")



DATABASE_NAME = "database.sqlite"

# Discord settings
EMBED_COLOUR = 0x3467eb

ADMIN_CHANNEL_ID = 1013130531220766852

TWEET_ROLE_NAME = "staff"
