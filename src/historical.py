import yfinance as yf
import pandas as pd 
from datetime import datetime 
import os

def get_historical_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)

    df.reset_index(inplace=True)
    df['Ticker'] = ticker
    return df


if __name__ == "__main__":
    ticker = "AAPL"
    start = "2023-01-01"
    end = datetime.today().strftime('%Y-%m-%d')

    df = get_historical_data(ticker, start, end)
    print(df.head())

    os.makedirs("data/raw", exist_ok=True)
    filename = f"data/raw/{ticker}_historical_{start}_to_{end}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved data to {filename}")
