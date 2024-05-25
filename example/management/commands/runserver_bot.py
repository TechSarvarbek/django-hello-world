import asyncio
import threading
import logging
from django.core.management.base import BaseCommand
from example.bot import main as bot_main  # Ensure this is the correct import path for your bot

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Run the aiogram bot concurrently with the Django server"

    def handle(self, *args, **kwargs):
        # Start the aiogram bot in a separate thread
        def start_bot():
            logger.info("Starting aiogram bot...")
            asyncio.run(bot_main())
        
        bot_thread = threading.Thread(target=start_bot)
        bot_thread.start()
