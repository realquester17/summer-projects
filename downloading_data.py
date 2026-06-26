import yfinance as yf
import pandas as pd
import os

# The 5 stocks we'll use for our backtesting project
tickers = {
    "RELIANCE.NS": "Reliance Industries",
    "TCS.NS": "Tata Consultancy Services",
    "HDFCBANK.NS": "HDFC Bank",
    "INFY.NS": "Infosys",
    "WIPRO.NS": "Wipro"
}

# Create a folder called 'data' inside your project
os.makedirs("data", exist_ok=True)

print("Downloading stock data...")
print("=" * 50)

for ticker, name in tickers.items():
    # Download 2 years of data
    data = yf.download(ticker, start="2022-01-01", end="2024-01-01")
    
    # Save as CSV file in the data folder
    filename = f"data/{ticker.replace('.NS', '')}_data.csv"
    data.to_csv(filename)
    
    print(f"✓ {name}")
    print(f"  Ticker: {ticker}")
    print(f"  Rows downloaded: {len(data)} trading days")
    print(f"  Saved to: {filename}")
    print()

print("=" * 50)
print("All data downloaded successfully.")
print("Check your 'data' folder — 5 CSV files are now there.")