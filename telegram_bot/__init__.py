from telegram.ext import Application

def create_bot(token: str):
    return Application.builder().token(token).build()
