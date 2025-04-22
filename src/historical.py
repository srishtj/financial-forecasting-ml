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


# getting sample data for models
tickers = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN"]
start = "2023-01-01"
end = datetime.today().strftime('%Y-%m-%d')

os.makedirs("data/sample", exist_ok=True)

for ticker in tickers:
    df = get_historical_data(ticker, start, end)
    filename = f"data/sample/{ticker}_historical_sample.csv"
    df.to_csv(filename, index=False)
    print(f"Saved sample data: {filename}")
