import multiprocessing
import os

def run_flask():
    os.system("python -m flask_app.app")

def run_telegram():
    os.system("python -m telegram_bot.main")

if __name__ == "__main__":
    flask_process = multiprocessing.Process(target=run_flask)
    telegram_process = multiprocessing.Process(target=run_telegram)

    flask_process.start()
    telegram_process.start()

    flask_process.join()
    telegram_process.join()
