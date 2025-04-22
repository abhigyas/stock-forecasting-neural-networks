
---

## `project_proposal.md`

```markdown
# Project Proposal  
## Title: Stock Price Forecasting Across Multiple Sectors Using Neural Networks

### Group Members:
- Abhigya Sinha
- Aniket Iyer
- Priyangshu Bhowmik
- Gautham Ande

---

## Objective
- Predict next-day stock returns or closing prices using neural networks.
- Compare performance across different market sectors (e.g., Technology, Finance, Energy).
- Evaluate both single-layer and multi-layer neural network architectures.

---

## Tools & Libraries
- `pandas`, `numpy`, `matplotlib`, `seaborn` — for data manipulation and visualization  
- `yfinance` — to retrieve stock data  
- `scikit-learn` — for data preprocessing, splitting, and evaluation metrics  
- `tensorflow.keras` or `torch.nn` — for neural network modeling  

---

## Data
- Source: Yahoo Finance via `yfinance`
- Time range: 2018–2024 (5+ years)
- Stocks from multiple sectors:
  - Technology: AAPL, MSFT  
  - Finance: JPM, BAC  
  - Energy: XOM, CVX  

---

## Features
- Lagged returns (1, 2, 3 days)
- 5-day and 10-day simple moving averages (SMA)
- Rolling standard deviation (volatility)
- Optional: sector/category flags or ETF benchmarks

---

## Modeling
- **Model 1**: Single-layer feedforward neural network
- **Model 2**: Multi-layer feedforward neural network (2–3 hidden layers with ReLU and optional dropout)
- Loss function: Mean Squared Error (MSE)
- Optimizer: Adam

---

## Evaluation
- Train/validation/test split using time-based sequence (no data leakage)
- Evaluation metrics:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R-squared (R²)
- Sector-wise comparison of model performance
- Visualizations: predicted vs actual price plots, error curves

---

## Stretch Goals
- Binary classification (predict up/down movement)
- Add macroeconomic indicators or ETF benchmarks as features
- Try early stopping or dropout for overfitting control
- Benchmark against naive forecast or ARIMA

---
