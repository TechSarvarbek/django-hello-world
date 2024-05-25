import asyncio
import logging
import threading
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management.base import BaseCommand
from example.bot import main as bot_main  # Assuming bot_main is the entry point for your aiogram bot

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Run Django server and aiogram bot concurrently"

    def handle(self, *args, **kwargs):
        # Function to start the Django server without the autoreloader
        def start_django():
            logger.info("Starting Django server...")
            runserver_command = RunserverCommand()
            runserver_command.run_from_argv([__name__, 'runserver', '--noreload'])

        # Start the Django server in a separate thread
        django_thread = threading.Thread(target=start_django)
        django_thread.start()

        # Start the aiogram bot in the main thread
        logger.info("Starting aiogram bot...")
        asyncio.run(bot_main())

