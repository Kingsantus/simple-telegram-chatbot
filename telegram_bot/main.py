from . import create_bot
from .bot import start_command, help_command, handle_message, error_handler
from telegram.ext import CommandHandler, MessageHandler, filters

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

def main():
    bot = create_bot(TOKEN)

    # Command handlers
    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(CommandHandler("help", help_command))

    # Message handlers
    bot.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    bot.add_error_handler(error_handler)

    print("Telegram bot started!")
    bot.run_polling()

if __name__ == "__main__":
    main()
