from telegram import Bot

BOT_TOKEN = "8180975507:AAHM8VIcjOA5dSFLnGF3ZSy-49mSLpfHr-M"
CHAT_ID = "8180975507"

def send_snapshot_to_telegram(image_path, message):
    bot = Bot(token=BOT_TOKEN)
    with open(image_path, 'rb') as img:
        bot.send_photo(chat_id=CHAT_ID, photo=img, caption=message)
