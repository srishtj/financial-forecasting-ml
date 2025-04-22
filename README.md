# financial-forecasting-ml
Scrapes financial market data and uses machine learning to analyze trends, forecast performance, and visualize insights.

## Features
- Web scraping with `requests` and `BeautifulSoup`
- Data cleaning & preprocessing
- Exploratory Data Analysis (EDA)
- ML models (regression, time series forecasting)
- Clean visualizations with `matplotlib` & `seaborn`

## Tech Stack
Python, pandas, NumPy, scikit-learn, matplotlib, BeautifulSoup, requests

## Setup Insturctions
1. Clone the repo:
git clone https://github.com/srishtj/financial-forecasting-ml
cd financial-forecasting-ml

2. Create and activate venv:
For mac users:
    python3 -m venv venv
    source venv/bin/activate

For windows users:
    python -m venv venv
    venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run sample data generator:
    python3 src/historical.py