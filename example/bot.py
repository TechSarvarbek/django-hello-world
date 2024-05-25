# bot.py
import logging
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from example.models import TelegramUser
from data.config import BOT_TOKEN, DOMAIN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    chat_id = message.chat.id
    user_obj, created = TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={"first_name": user.first_name}
    )
    logger.info(f"User: {user_obj}, created: {created}")

    webapp_button = telebot.types.InlineKeyboardButton("Open WebApp", url=DOMAIN)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(webapp_button)

    bot.send_message(
        chat_id=chat_id,
        text=f"Hello, {user.first_name}!",
        reply_markup=keyboard
    )

def start_handler():
    print("OK")

def run_dispatcher():
    bot.polling()

if __name__ == "__main__":
    run_dispatcher()    
