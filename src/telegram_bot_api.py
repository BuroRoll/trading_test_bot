import requests

from settings import settings


class TelegramBot:
    def __init__(self):
        self.chat_id = settings.TELEGRAM_CHAT_ID
        self.api_url = f'https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/sendMessage'

    def send_message(self, message: str) -> None:
        requests.get(self.api_url, params={'text': message, 'chat_id': self.chat_id})
