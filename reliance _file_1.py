import yfinance as yf
import matplotlib.pyplot as plt

stock = yf.download("RELIANCE.NS", start="2024-01-01", end="2025-01-01")
plt.figure(figsize=(12,6))
plt.plot(stock['Close'])
plt.title("Reliance Industries - 1 Year Price")
plt.xlabel("Date")
plt.ylabel("Price (₹)")
plt.grid(True)
plt.show()