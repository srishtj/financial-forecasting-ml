# financial-forecasting-ml
Scrapes financial market data and uses machine learning to analyze trends, forecast performance, and visualize insights.

You can use ready-to-use sample datasets, run data exploration notebooks (`eda.ipynb`), train models, and compare actual vs predicted prices.

## Features
- Web scraping with `requests` and `BeautifulSoup`
- Historical data retrieval using `yfinance`
- Sample datasets preloaded in `data/sample` for instant demo
- Exploratory Data Analysis (EDA)
- ML models (linear regression, time series forecasting)
- Performance metrics and visualisations
- Clean visualizations with `matplotlib` & `seaborn`

## Tech Stack
Python, pandas, NumPy, scikit-learn, matplotlib, BeautifulSoup, requests

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/srishtj/financial-forecasting-ml
   cd financial-forecasting-ml
   ```

2. Create and activate venv:

   For mac users:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For windows users:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run sample data generator:
   ```bash
   python3 src/historical.py
   ```

## Sample Data & Usage

This repo includes pre-saved historical stock data under `data/sample/` for multiple tickers (AAPL, TSLA, GOOGL, etc.)
You can immediately run analysis and modeling notebooks using these datasets.

### How to Use
- Explore stock performance and trends in `notebooks/eda.ipynb`
- Train a predictive model in `notebooks/modeling.ipynb`
- Compare actual vs predicted prices, and view error margins
- Modify the scripts in `src/` to add your own tickers or update data
- Use `scraper.py` to access real-time data
