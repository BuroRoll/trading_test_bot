from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # BINANCE_API_KEY = ''
    # BINANCE_SECRET_KEY = ''
    TELEGRAM_API_TOKEN: str = ''
    TELEGRAM_CHAT_ID: str = ''
    TICKET: str = 'ETH-USD'
    START_BALANCE_USD: float = 100
    BUYING_MACD_VALUE: int = 3


settings = Settings()
