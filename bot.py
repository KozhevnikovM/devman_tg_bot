from telegram import Bot
from config import TELEGRAM_BOT_API_KEY


def send_telegram_message(chat_id, text):
    bot = Bot(token=TELEGRAM_BOT_API_KEY)
    bot.send_message(chat_id=chat_id, text=text)


if __name__ == '__main__':
    from config import TELEGRAM_CHAT_ID
    send_telegram_message('test', TELEGRAM_CHAT_ID)