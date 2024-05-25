import logging
import threading
import telebot
from django.core.management.commands.runserver import Command as RunserverCommand
from example.bot import run_dispatcher
from data.config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class Command(RunserverCommand):
    def handle(self, *args, **options):
        # Function to start the Django server without the autoreloader
        def start_django(*args, **options):
            logger.info("Starting Django server...")
            options['use_reloader'] = False  # Disable the autoreloader
            super(Command, self).handle(*args, **options)  # Explicitly pass the class and self

        # Start the Django server in a separate thread
        django_thread = threading.Thread(target=start_django, args=args, kwargs=options)
        django_thread.start()

        # Start the telegram bot
        logger.info("Starting telegram bot...")
        run_dispatcher()