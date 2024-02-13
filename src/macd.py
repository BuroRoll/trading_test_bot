import pandas as pd
import yfinance as yf


def calculate_macd(df):
    # Вычисление экспоненциальных скользящих средних
    df['ema12'] = df['Close'].ewm(span=12, adjust=False, min_periods=12).mean()
    # Get the 12-day EMA of the closing price
    df['ema26'] = df['Close'].ewm(span=26, adjust=False, min_periods=26).mean()
    # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
    df['macd'] = df['ema12'] - df['ema26']
    # Get the 9-Day EMA of the MACD for the Trigger line
    df['macd_signal'] = df['macd'].ewm(span=9).mean()
    # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
    df['macd_histogram'] = df['macd'] - df['macd_signal']
    return df


def calc_macd_value(ticket):
    data = yf.download(ticket, period='1y', interval="1h", progress=False)
    data['Date'] = data.index
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    df = calculate_macd(data)
    return df['macd_histogram'].iloc[-1]


# if __name__ == '__main__':
#     calc_macd_value()
