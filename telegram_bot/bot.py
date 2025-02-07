import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from flask_app.chatbot import get_bot_response

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm Cyborg! I'm here to help with all your programming and coding questions.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I'm an AI assistant here to help with your programming and coding questions. "
        "Just type in your question, and I'll do my best to assist you!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = get_bot_response(text)
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
