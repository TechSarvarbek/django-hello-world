import asyncio
import logging
import threading
import os
from django.core.management import execute_from_command_line
from example.bot import main as bot_main

logger = logging.getLogger(__name__)

class RunserverWithBotCommand:
    def handle(self):
        # Function to start the Django server without the autoreloader
        def start_django():
            logger.info("Starting Django server...")
            execute_from_command_line(['manage.py', 'runserver', '--noreload'])

        # Start the Django server in a separate thread
        django_thread = threading.Thread(target=start_django)
        django_thread.start()

        # Start the aiogram bot in the
        #  main thread
        logger.info("Starting aiogram bot...")
        asyncio.run(bot_main())

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    command = RunserverWithBotCommand()
    command.handle()