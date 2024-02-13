import yfinance as yf

from macd import calc_macd_value
from settings import settings
from telegram_bot_api import TelegramBot


class Trading:
    def __init__(self):
        self.balance_usd = settings.START_BALANCE_USD
        self.balance_crypto = 0
        self.status = 'SELL'
        self.ticket_pair = settings.TICKET
        self.telegram_bot = TelegramBot()

    def get_ticket_price(self):
        ticket = yf.Ticker(self.ticket_pair)
        today_data = ticket.history(interval="1m", period="1d")
        return today_data['Close'].iloc[-1]

    def trade(self):
        macd_status = calc_macd_value(self.ticket_pair)
        macd_indicator = 'BUY' if macd_status > 0 else 'SELL'
        if macd_indicator == self.status:
            return
        ticket_price = self.get_ticket_price()
        if macd_indicator == 'BUY':
            self.buy(ticket_price)
        elif macd_indicator == 'SELL':
            self.sell(ticket_price)
        self.send_stat()

    def sell(self, current_price):
        self.balance_usd = self.balance_crypto * current_price
        self.balance_crypto = 0
        self.status = 'SELL'

    def buy(self, current_price):
        self.balance_crypto = self.balance_usd / current_price
        self.balance_usd = 0
        self.status = 'BUY'

    def send_stat(self):
        stat = (f'Current stat:\n'
                f'{self.ticket_pair=}\n'
                f'{self.status=}\n'
                f'{self.balance_usd=}\n'
                f'{self.balance_crypto=}')
        self.telegram_bot.send_message(stat)

    def print_stat(self):
        print(f'Current stat:\n'
              f'{self.ticket_pair=}\n'
              f'{self.balance_usd=}\n'
              f'{self.balance_crypto=}')

    def get_stat_string(self):
        return (f'Current stat:\n'
                f'{self.ticket_pair=}\n'
                f'{self.balance_usd=}\n'
                f'{self.balance_crypto=}')
