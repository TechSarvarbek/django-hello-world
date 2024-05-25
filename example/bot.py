import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.types import Message
from data.config import BOT_TOKEN, ADMINS, DOMAIN

from .models import TelegramUser
from asgiref.sync import sync_to_async

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Command handler for /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Use sync_to_async for Django ORM operations
    user, created = await sync_to_async(TelegramUser.objects.get_or_create)(
        chat_id=message.chat.id,
        defaults={'first_name': message.chat.first_name}
    )
    print(user, created)
    webapp_button = InlineKeyboardButton(text="Open WebApp", web_app=WebAppInfo(url=DOMAIN))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=keyboard)

@dp.startup()
async def on_startup():
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text="Bot ishga tushdi🟢")

@dp.shutdown()
async def on_shutdown():
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text="Bot to'xtadi🔴")

async def main() -> None:
    logger.info("Starting bot polling...")
    await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)

if __name__ == "__main__":
    asyncio.run(main())
