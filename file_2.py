import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download Reliance data
stock = yf.download("RELIANCE.NS", start="2024-01-01", end="2025-01-01")

# ── DAILY RETURNS ─────────────────────────────────────────
# pct_change() calculates % change from previous day
# Multiply by 100 to get percentage instead of decimal
stock['Daily_Return'] = stock['Close'].pct_change() * 100

# ── MOVING AVERAGE ────────────────────────────────────────
# rolling(20) takes a 20 day window and calculates average
# This smooths out daily noise and shows the trend
stock['MA20'] = stock['Close'].rolling(window=20).mean()

# Also add 9 EMA and 21 EMA since you're already using these
# EMA gives more weight to recent prices than simple average
stock['EMA9'] = stock['Close'].ewm(span=9).mean()
stock['EMA21'] = stock['Close'].ewm(span=21).mean()

# ── PLOT PRICE WITH MOVING AVERAGES ──────────────────────
plt.figure(figsize=(14,7))
plt.plot(stock['Close'], label='Close Price', alpha=0.7)
plt.plot(stock['MA20'], label='20 Day MA', color='orange')
plt.plot(stock['EMA9'], label='9 EMA', color='green', linestyle='--')
plt.plot(stock['EMA21'], label='21 EMA', color='red', linestyle='--')
plt.title("Reliance — Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (₹)")
plt.legend()
plt.grid(True)
plt.show()

# ── BASIC STATISTICS ─────────────────────────────────────
print("=" * 40)
print("RELIANCE STATISTICS")
print("=" * 40)
print(f"Average daily return: {round(stock['Daily_Return'].mean(), 3)}%")
print(f"Best single day:      {round(stock['Daily_Return'].max(), 3)}%")
print(f"Worst single day:     {round(stock['Daily_Return'].min(), 3)}%")
print(f"Volatility (std dev): {round(stock['Daily_Return'].std(), 3)}%")
print(f"Total data points:    {len(stock)} trading days")