import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

def plot_predictions(y_true, y_pred, title="Prediction vs Actual"):
    plt.figure(figsize=(10, 4))
    plt.plot(y_true.values, label="Actual")
    plt.plot(y_pred, label="Predicted")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Return")
    plt.legend()
    plt.grid(True)
    plt.show()

def compute_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2
