import pandas as pd
import matplotlib.pyplot as plt

names = {
    "RELIANCE": "Reliance",
    "TCS": "TCS",
    "HDFCBANK": "HDFC Bank",
    "INFY": "Infosys",
    "WIPRO": "Wipro"
}

stocks = {}
print("Loading all stocks...")
print("=" * 65)
print(f"{'Stock':<15} {'Avg Return':<15} {'Volatility':<15} {'Best Day':<12} {'Worst Day'}")
print("=" * 65)

for ticker, name in names.items():
    # skiprows=1 skips the extra header yfinance adds
    df = pd.read_csv(
        f"data/{ticker}_data.csv",
        skiprows=[1],          # skip the weird second header row
        index_col=0,
        parse_dates=True
    )
    
    # Force Close column to numeric — fixes the string error
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    
    # Drop any rows where Close is NaN
    df = df.dropna(subset=['Close'])
    
    # Calculate daily returns
    df['Daily_Return'] = df['Close'].pct_change() * 100
    
    stocks[ticker] = df
    
    avg   = round(df['Daily_Return'].mean(), 3)
    vol   = round(df['Daily_Return'].std(), 3)
    best  = round(df['Daily_Return'].max(), 3)
    worst = round(df['Daily_Return'].min(), 3)
    
    print(f"{name:<15} {avg:<15} {vol:<15} {best:<12} {worst}")

print("=" * 65)

# Plot all 5 normalized
plt.figure(figsize=(14,7))

for ticker, name in names.items():
    df = stocks[ticker]
    normalized = (df['Close'] / df['Close'].iloc[0]) * 100
    plt.plot(normalized, label=name)

plt.title("5 Nifty Stocks — 2 Year Normalized Performance")
plt.xlabel("Date")
plt.ylabel("Normalized Price (Base 100)")
plt.legend()
plt.grid(True)
plt.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
plt.show()