from telegram.ext import Application

# instantiate bot
def create_bot(token: str):
    return Application.builder().token(token).build()
