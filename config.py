from dotenv import load_dotenv
import os

load_dotenv()
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TELEGRAM_BOT_API_KEY = os.getenv('TELEGRAM_BOT_API_KEY')

TELEGRAM_CHAT_ID = 312873002