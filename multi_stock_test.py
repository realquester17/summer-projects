import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

tickers = {
    "RELIANCE": "Reliance",
    "TCS": "TCS",
    "HDFCBANK": "HDFC Bank",
    "INFY": "Infosys",
    "WIPRO": "Wipro"
}

results = {}
print("=" * 55)
print(f"{'Stock':<15} {'Buy&Hold':<15} {'EMA Strategy':<15} {'Winner'}")
print("=" * 55)

plt.figure(figsize=(14,7))

for ticker, name in tickers.items():
    df = pd.read_csv(
        f"data/{ticker}_data.csv",
        skiprows=[1], index_col=0,
        parse_dates=True, date_format="%Y-%m-%d"
    )
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna(subset=['Close'])

    df['EMA9']  = df['Close'].ewm(span=9,  adjust=False).mean()
    df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
    df['Position'] = 0
    df.loc[df['EMA9'] > df['EMA21'], 'Position'] = 1

    df['Daily_Return']    = df['Close'].pct_change()
    df['Strategy_Return'] = df['Daily_Return'] * df['Position'].shift(1)

    df['BH_Cum']  = (1 + df['Daily_Return']).cumprod() * 100
    df['Str_Cum'] = (1 + df['Strategy_Return']).cumprod() * 100

    bh_final  = round(df['BH_Cum'].iloc[-1], 2)
    str_final = round(df['Str_Cum'].iloc[-1], 2)
    winner    = "Strategy" if str_final > bh_final else "Buy&Hold"

    print(f"{name:<15} ₹{bh_final:<14} ₹{str_final:<14} {winner}")
    results[name] = {'bh': bh_final, 'strategy': str_final}

    plt.plot(df['Str_Cum'], label=name)

print("=" * 55)

plt.title("9/21 EMA Strategy — All 5 Stocks")
plt.xlabel("Date")
plt.ylabel("Portfolio Value (Starting ₹100)")
plt.legend()
plt.grid(True)
plt.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
plt.show()

# Calculate how "trending" each stock was
# A simple way: total return divided by volatility
# Higher number = smoother trend, Lower number = choppier movement

print("\n" + "=" * 55)
print("TREND STRENGTH ANALYSIS")
print("=" * 55)

for ticker, name in tickers.items():
    df = pd.read_csv(
        f"data/{ticker}_data.csv",
        skiprows=[1], index_col=0,
        parse_dates=True, date_format="%Y-%m-%d"
    )
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna(subset=['Close'])
    df['Daily_Return'] = df['Close'].pct_change()

    total_return = (df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100
    volatility = df['Daily_Return'].std() * 100

    # Trend strength = return per unit of volatility
    trend_strength = round(total_return / volatility, 3) if volatility != 0 else 0

    print(f"{name:<15} Total Return: {round(total_return,2)}%   "
          f"Volatility: {round(volatility,3)}%   "
          f"Trend Strength: {trend_strength}")
print("\n" + "=" * 60)
print("DETAILED COMPARISON")
print("=" * 60)

for ticker, name in tickers.items():
    df = pd.read_csv(
        f"data/{ticker}_data.csv",
        skiprows=[1], index_col=0,
        parse_dates=True, date_format="%Y-%m-%d"
    )
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna(subset=['Close'])

    df['EMA9']  = df['Close'].ewm(span=9,  adjust=False).mean()
    df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
    df['Position'] = 0
    df.loc[df['EMA9'] > df['EMA21'], 'Position'] = 1

    df['Daily_Return']    = df['Close'].pct_change()
    df['Strategy_Return'] = df['Daily_Return'] * df['Position'].shift(1)

    bh_final  = round((1 + df['Daily_Return']).cumprod().iloc[-1] * 100, 2)
    str_final = round((1 + df['Strategy_Return']).cumprod().iloc[-1] * 100, 2)

    print(f"{name:<15} Buy&Hold: ₹{bh_final:<10} Strategy: ₹{str_final:<10} "
          f"Both profitable: {bh_final > 100 and str_final > 100}")