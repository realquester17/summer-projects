import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Download both stocks
print("Downloading data...")
reliance = yf.download("RELIANCE.NS", start="2024-01-01", end="2025-01-01")
tcs = yf.download("TCS.NS", start="2024-01-01", end="2025-01-01")

# Calculate daily returns for both
reliance['Daily_Return'] = reliance['Close'].pct_change() * 100
tcs['Daily_Return'] = tcs['Close'].pct_change() * 100

# ── PRINT COMPARISON ─────────────────────────────────────
print("\n" + "=" * 40)
print("STOCK COMPARISON")
print("=" * 40)

print("\nRELIANCE:")
print(f"  Average daily return: {round(reliance['Daily_Return'].mean(), 3)}%")
print(f"  Volatility:           {round(reliance['Daily_Return'].std(), 3)}%")
print(f"  Best day:             {round(reliance['Daily_Return'].max(), 3)}%")
print(f"  Worst day:            {round(reliance['Daily_Return'].min(), 3)}%")

print("\nTCS:")
print(f"  Average daily return: {round(tcs['Daily_Return'].mean(), 3)}%")
print(f"  Volatility:           {round(tcs['Daily_Return'].std(), 3)}%")
print(f"  Best day:             {round(tcs['Daily_Return'].max(), 3)}%")
print(f"  Worst day:            {round(tcs['Daily_Return'].min(), 3)}%")

# ── CORRELATION ───────────────────────────────────────────
# Correlation ranges from -1 to +1
# +1 means they move perfectly together
# 0 means no relationship
# -1 means they move in opposite directions
correlation = reliance['Daily_Return'].corr(tcs['Daily_Return'])
print(f"\nCorrelation between Reliance and TCS: {round(correlation, 3)}")

if correlation > 0.7:
    print("Interpretation: HIGH correlation — they move very similarly")
elif correlation > 0.4:
    print("Interpretation: MODERATE correlation — some relationship")
else:
    print("Interpretation: LOW correlation — they move independently")

# ── PLOT BOTH PRICES NORMALIZED ──────────────────────────
# Normalize to 100 so we can compare them on same scale
# regardless of different price levels
reliance_norm = (reliance['Close'] / reliance['Close'].iloc[0]) * 100
tcs_norm = (tcs['Close'] / tcs['Close'].iloc[0]) * 100

plt.figure(figsize=(14,7))
plt.plot(reliance_norm, label='Reliance', color='blue')
plt.plot(tcs_norm, label='TCS', color='orange')
plt.title("Reliance vs TCS — Normalized Performance (Base 100)")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend()
plt.grid(True)
plt.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
plt.show()