import threading
import time
import schedule

from telegram_bot_api import TelegramBot
from trading import Trading


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def log_day_results(trading: Trading, telegram_bot: TelegramBot):
    telegram_bot.send_message(trading.get_stat_string())


if __name__ == '__main__':
    trading = Trading()
    telegram_bot = TelegramBot()
    schedule.every(1).minute.do(run_threaded, trading.trade)
    schedule.every(1).day.do(run_threaded, log_day_results, trading=trading, telegram_bot=telegram_bot)

    while True:
        schedule.run_pending()
        time.sleep(1)
