from telegram import Bot
from config import TG_BOT_API_KEY

def tg_send_message(text):
    bot = Bot(token=TG_BOT_API_KEY)
    bot.send_message(chat_id=312873002, text=text)