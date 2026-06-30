# Indian Equity EMA Strategy Backtester

A Python-based backtesting framework that tests a 9/21 EMA crossover 
trading strategy against simple Buy-and-Hold across 5 major Nifty 50 
stocks, evaluating both raw returns and risk-adjusted performance.

## Project Background

Built while learning Python, data analysis, and stock market fundamentals 
as a first-year EEE student. The goal was to test whether a simple, 
commonly used technical strategy (9/21 EMA crossover, used in my own 
paper trading) actually beats just holding the stock — using real 
historical data instead of assumptions.

## Key Finding

EMA 9/21 crossover does NOT consistently outperform Buy-and-Hold. It 
only beat Buy-and-Hold on 2 out of 5 stocks tested — specifically on 
stocks that were in a strong downtrend (Infosys, Wipro), where the 
strategy provided downside protection by exiting before major declines. 
On stocks in strong uptrends (Reliance, HDFC Bank), Buy-and-Hold won 
because the strategy's lagging signals caused it to miss portions of 
the rally.

**Conclusion:** EMA crossover works better as a downside protection 
mechanism during downtrends, not as a strategy to maximize gains during 
uptrends. This was confirmed using both raw returns and Sharpe ratio 
(risk-adjusted returns).

## What's Inside

| File | Purpose |
|---|---|
| `stock_class.py` | OOP practice — Stock and IndexStock classes |
| `numpy_practice.py` | Numpy fundamentals — arrays, indexing, statistics |
| `pandas_practice/` | Pandas fundamentals — DataFrames, filtering, grouping |
| `matplotlib_practice.py` | Data visualization fundamentals |
| `first_stock_chart.py` | First real stock chart — Reliance price plotted using yfinance |
| `file_2.py` | Daily returns, moving averages, and volatility for a single stock |
| `file_3.py` | Comparing two stocks — returns, volatility, and correlation |
| `downloading_data.py` | Downloads and saves 2 years of data for 5 Nifty stocks |
| `project_analysis_v1.py` | Loads saved data, calculates statistics across all 5 stocks |
| `ema_strategy.py` | Calculates 9/21 EMA crossover signals and visualizes buy/sell points |
| `backtester_v1.py` | Backtests EMA strategy vs Buy-and-Hold on a single stock |
| `multi_stock_test.py` | Runs the backtest across all 5 stocks for generalization testing |
| `sharpe_analysis.py` | Calculates risk-adjusted returns (Sharpe ratio) for all 5 stocks |
| `drawdown_analysis.py` | Measures maximum drawdown — worst-case loss from peak |

## Tools and Libraries Used

Python · Pandas · NumPy · Matplotlib · yfinance

## What I'm Currently Learning

- Zerodha Varsity — Technical and Fundamental Analysis
- TryHackMe — Networking and Linux fundamentals  
- LeetCode — Data Structures and Algorithms basics

## Next Steps

- Explore alternative strategies (RSI, volume-based signals) using the 
  same backtesting framework
- Combine fundamental analysis with technical signals
- Build a simple portfolio-level backtest across multiple stocks held 
  simultaneously