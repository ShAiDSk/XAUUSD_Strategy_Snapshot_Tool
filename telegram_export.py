from telegram import Bot

BOT_TOKEN = "Token"
CHAT_ID = "ID"

def send_snapshot_to_telegram(image_path, message):
    bot = Bot(token=BOT_TOKEN)
    with open(image_path, 'rb') as img:
        bot.send_photo(chat_id=CHAT_ID, photo=img, caption=message)
