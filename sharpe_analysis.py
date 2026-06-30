import pandas as pd
import numpy as np

tickers = {
    "RELIANCE": "Reliance",
    "TCS": "TCS",
    "HDFCBANK": "HDFC Bank",
    "INFY": "Infosys",
    "WIPRO": "Wipro"
}

# Risk free rate in India (approximate)
# Based on current RBI repo rate
RISK_FREE_RATE = 0.065  # 6.5% annually

def calculate_sharpe(returns, risk_free_rate=RISK_FREE_RATE):
    # Convert annual risk free rate to daily
    daily_rf = risk_free_rate / 252  # 252 trading days in a year
    
    # Excess return = strategy return minus risk free return
    excess_returns = returns - daily_rf
    
    # Sharpe = average excess return / std of excess returns
    # Multiply by sqrt(252) to annualize
    if returns.std() == 0:
        return 0
    sharpe = (excess_returns.mean() / returns.std()) * np.sqrt(252)
    return round(sharpe, 3)

print("=" * 70)
print(f"{'Stock':<15} {'BH Sharpe':<15} {'Strategy Sharpe':<18} {'Better Strategy?'}")
print("=" * 70)

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

    bh_sharpe  = calculate_sharpe(df['Daily_Return'].dropna())
    str_sharpe = calculate_sharpe(df['Strategy_Return'].dropna())
    better     = "Yes" if str_sharpe > bh_sharpe else "No"

    print(f"{name:<15} {bh_sharpe:<15} {str_sharpe:<18} {better}")

print("=" * 70)
print("\nSharpe Ratio interpretation:")
print("  > 1.0  : Good")
print("  > 1.5  : Very good")
print("  > 2.0  : Excellent")
print("  < 0    : Strategy losing money vs risk free rate")
'''"Risk-adjusted analysis using Sharpe ratio confirms the earlier finding: EMA 9/21 crossover outperforms Buy and Hold specifically during strong downtrends, both in raw returns and risk-adjusted terms. The strategy does not generate high positive Sharpe ratios anywhere — even on its 'winning' stocks Wipro (0.005) and Infosys (-0.341), the Sharpe ratios are weak or negative. This means EMA crossover is not a strategy for generating strong risk-adjusted returns — its real value is capital preservation during downtrends, converting severely negative Sharpe ratios into near-neutral ones. On trending-up stocks like Reliance and HDFC Bank, Buy and Hold remains clearly superior on a risk-adjusted basis."'''