import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

stock = yf.download("RELIANCE.NS", start="2022-01-01", end="2024-01-01")
# Flatten columns in case yfinance returns multi-level columns
if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

stock['Close'] = pd.to_numeric(stock['Close'], errors='coerce')
stock = stock.dropna(subset=['Close'])

# Calculate EMAs
stock['EMA9']  = stock['Close'].ewm(span=9,  adjust=False).mean()
stock['EMA21'] = stock['Close'].ewm(span=21, adjust=False).mean()

# Strategy: hold stock when EMA9 > EMA21, cash otherwise
stock['Position'] = 0
stock.loc[stock['EMA9'] > stock['EMA21'], 'Position'] = 1

# Daily return of stock
stock['Daily_Return'] = stock['Close'].pct_change()

# Strategy return = stock return only when we're holding (Position=1)
# Shift(1) means use yesterday's position for today's return
# (you can't know today's signal until today's close)
stock['Strategy_Return'] = stock['Daily_Return'] * stock['Position'].shift(1)

# Cumulative returns — how ₹100 grows over time
stock['Buy_Hold_Cumulative']  = (1 + stock['Daily_Return']).cumprod() * 100
stock['Strategy_Cumulative']  = (1 + stock['Strategy_Return']).cumprod() * 100

# Plot comparison
plt.figure(figsize=(14,7))
plt.plot(stock['Buy_Hold_Cumulative'],
         label='Buy and Hold', color='blue')
plt.plot(stock['Strategy_Cumulative'],
         label='9/21 EMA Strategy', color='green')
plt.title("9/21 EMA Strategy vs Buy and Hold — Reliance 2022-2024")
plt.xlabel("Date")
plt.ylabel("Portfolio Value (Starting ₹100)")
plt.legend()
plt.grid(True)
plt.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
plt.show()

# Final results
final_bh  = round(stock['Buy_Hold_Cumulative'].iloc[-1], 2)
final_str = round(stock['Strategy_Cumulative'].iloc[-1], 2)

print("=" * 45)
print("BACKTEST RESULTS — Reliance 2022-2024")
print("=" * 45)
print(f"Buy and Hold final value:    ₹{final_bh}")
print(f"EMA Strategy final value:    ₹{final_str}")
print(f"Strategy outperforms:        {final_str > final_bh}")