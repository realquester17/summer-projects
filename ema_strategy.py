import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download Reliance data
stock = yf.download("RELIANCE.NS", start="2022-01-01", end="2024-01-01")
# Flatten columns in case yfinance returns multi-level columns
if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

stock['Close'] = pd.to_numeric(stock['Close'], errors='coerce')
stock = stock.dropna(subset=['Close'])


# Calculate 9 and 21 EMA — exactly what you use in paper trading
stock['EMA9']  = stock['Close'].ewm(span=9,  adjust=False).mean()
stock['EMA21'] = stock['Close'].ewm(span=21, adjust=False).mean()

# Generate signals
# When EMA9 crosses above EMA21 = Buy signal (1)
# When EMA9 crosses below EMA21 = Sell signal (-1)
stock['Signal'] = 0
stock.loc[stock['EMA9'] > stock['EMA21'], 'Signal'] = 1
stock.loc[stock['EMA9'] < stock['EMA21'], 'Signal'] = -1

# Find actual crossover points
stock['Crossover'] = stock['Signal'].diff()

# Plot
plt.figure(figsize=(14,7))
plt.plot(stock['Close'], label='Close Price', alpha=0.7, color='blue')
plt.plot(stock['EMA9'],  label='EMA 9',  color='green', linewidth=1.5)
plt.plot(stock['EMA21'], label='EMA 21', color='red',   linewidth=1.5)

# Mark buy signals with green triangles
buy_signals = stock[stock['Crossover'] == 2]
plt.scatter(buy_signals.index, buy_signals['Close'],
            marker='^', color='green', s=100, label='Buy Signal', zorder=5)

# Mark sell signals with red triangles
sell_signals = stock[stock['Crossover'] == -2]
plt.scatter(sell_signals.index, sell_signals['Close'],
            marker='v', color='red', s=100, label='Sell Signal', zorder=5)

plt.title("Reliance — 9/21 EMA Crossover Strategy")
plt.xlabel("Date")
plt.ylabel("Price (₹)")
plt.legend()
plt.grid(True)
plt.show()

# Count signals
print(f"Total buy signals:  {len(buy_signals)}")
print(f"Total sell signals: {len(sell_signals)}")