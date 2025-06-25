import os
from dotenv import load_dotenv

load_dotenv()  # pulls vars from .env into the process

TELEGRAM_API_ID = int(os.getenv("TELEGRAM_API_ID"))
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

IMAGE_PATH = 'images/r030.jpg'