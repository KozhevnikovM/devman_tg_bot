from dotenv import load_dotenv
import os

load_dotenv()
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TG_BOT_API_KEY = os.getenv('TG_BOT_API_KEY')