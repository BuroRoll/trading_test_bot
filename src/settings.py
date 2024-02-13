from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # BINANCE_API_KEY = ''
    # BINANCE_SECRET_KEY = ''
    TELEGRAM_API_TOKEN: str = ''
    TELEGRAM_CHAT_ID: str = ''
    TICKET: str = 'ETH-USD'
    START_BALANCE_USD: float = 10_000


settings = Settings()
