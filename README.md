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