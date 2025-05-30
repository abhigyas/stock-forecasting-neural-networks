# Stock Price Forecasting Using Neural Networks

### Group Members:
- Abhigya Sinha
- Aniket Iyer
- Priyangshu Bhowmik
- Gautham Ande

---

## Overview

This project aims to predict short-term stock price movements using feedforward neural networks, applying both single-layer and multi-layer architectures. Historical stock data is collected from Yahoo Finance for companies across multiple sectors including Technology, Finance, and Energy. Time series features like lagged returns, moving averages, and rolling volatility are engineered to train the models.

Our goal is to evaluate how well neural networks can generalize across different industries, and compare their performance using standard regression metrics.

---

## Technologies Used

- Python 3.x  
- TensorFlow / PyTorch  
- scikit-learn  
- pandas, numpy, matplotlib, seaborn  
- yfinance (for stock data)

---

## Project Structure

```
stock-forecasting-neural-networks/
├── README.md PLEASE READ
├── project_proposal.md
├── written_report_clean.docx WORD FORMAT WRITE UP
├── written_report_clean.pdf PDF FORMAT WRITE UP
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── plots/
│   ├── data_plots/
│   └── model_plots/
├── notebooks/ USE THIS TO RUN CODE, RUN THEM IN ORDER FROM 01-04 (just click run all on each notebook) (WRITEUP HAS ALL THE SOURCE CODE WITH DETAILED COMMENTS)
│   ├── 01_data_collection_and_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling_single_layer_nn.ipynb
│   └── 04_modeling_multi_layer_nn.ipynb
├── utils/
│   └── preprocessing.py
│   └── __init__.py
│   └── evaluation.py
└── models/
    └── saved_model/
```

---

## Setup Instructions

1. Clone the repository (If fetching from github):
```bash
git clone https://github.com/abhigyas/stock-forecasting-neural-networks.git
cd stock-forecasting-neural-networks
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Jupyter notebooks in the `/notebooks/` folder step-by-step.

---

## Outputs

- Trained models (saved in `/models/`)
- Evaluation plots (predicted vs actual)
- Metrics (MAE, RMSE, R²)
- Final report (`written_report.docx`) with code explanations
