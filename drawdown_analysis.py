import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = "RELIANCE"
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

# Cumulative wealth
df['BH_Cum']  = (1 + df['Daily_Return']).cumprod()
df['Str_Cum'] = (1 + df['Strategy_Return']).cumprod()

# Maximum drawdown calculation
# Rolling maximum = highest point seen so far
# Drawdown = how far below that peak we currently are
df['BH_Peak']       = df['BH_Cum'].cummax()
df['BH_Drawdown']   = (df['BH_Cum'] - df['BH_Peak']) / df['BH_Peak'] * 100

df['Str_Peak']      = df['Str_Cum'].cummax()
df['Str_Drawdown']  = (df['Str_Cum'] - df['Str_Peak']) / df['Str_Peak'] * 100

# Plot drawdowns
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14,10))

ax1.fill_between(df.index, df['BH_Drawdown'],
                 0, alpha=0.4, color='blue', label='Buy and Hold')
ax1.fill_between(df.index, df['Str_Drawdown'],
                 0, alpha=0.4, color='green', label='EMA Strategy')
ax1.set_title("Drawdown Comparison — Reliance")
ax1.set_ylabel("Drawdown (%)")
ax1.legend()
ax1.grid(True)

ax2.plot(df['BH_Cum'] * 100,  label='Buy and Hold', color='blue')
ax2.plot(df['Str_Cum'] * 100, label='EMA Strategy',  color='green')
ax2.set_title("Cumulative Returns")
ax2.set_ylabel("Portfolio Value (₹100 start)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

print(f"Max Drawdown — Buy and Hold:   {round(df['BH_Drawdown'].min(), 2)}%")
print(f"Max Drawdown — EMA Strategy:   {round(df['Str_Drawdown'].min(), 2)}%")