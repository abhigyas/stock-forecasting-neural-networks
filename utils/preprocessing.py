import pandas as pd

def generate_features(df):
    df['Return'] = df['Close'].pct_change()
    df['Lag_1'] = df['Return'].shift(1)
    df['Lag_2'] = df['Return'].shift(2)
    df['Lag_3'] = df['Return'].shift(3)
    df = df.dropna()
    return df

def prepare_data(df):
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna()
    X = df.drop(columns=['Return'])
    y = df['Return'].shift(-1).dropna()
    X = X.iloc[:-1]
    return X, y
