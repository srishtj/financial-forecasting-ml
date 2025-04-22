import requests
from bs4 import BeautifulSoup

def get_stock_detail(ticker):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

    url = f'https://finance.yahoo.com/quote/{ticker}/'
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    price_span = soup.find('span', {'data-testid': 'qsp-price'})

    if price_span:
        price = price_span.text.strip()
        print(f"Current {ticker} Price: {price}")
        return float(price.replace(',', ''))
    else:
        print("Price not found ")
        return None

get_stock_detail('AAPL')
get_stock_detail('TSLA')
get_stock_detail('AMZN')
