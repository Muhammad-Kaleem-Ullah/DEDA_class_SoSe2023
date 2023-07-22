import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

def test_model(scaled_data, training_data_len, window_size, dataset, model, unit):
    test_data = scaled_data[training_data_len - num_features:, :]
    X_test = []
    y_test = dataset[training_data_len:, :]

    for i in range(num_features, len(test_data)):
        X_test.append(test_data[i - num_features: i, 0])
    
    
    
    X_test = np.array(X_test)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
    
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    
    rmse = np.sqrt(np.mean((y_test - predictions) ** 2))
    print(f"Mean Absolute Error = {mean_absolute_error(y_test, predictions)}")
    print(f"Root Mean Squared Error RMSE = {rmse}")
    print(f"Mean Squared Error RMSE = {mean_squared_error(y_test, predictions)}")
    
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid["Predictions"] = predictions
    
    
    plt.figure(figsize = (16, 8))
    #plt.title("Model")
    plt.xlabel("Date", fontsize = 18)
    plt.ylabel(f"BitCoin's Close {unit}", fontsize = 18)
    plt.grid(False)
    plt.plot(train["Close"])
    plt.plot(valid[["Close", "Predictions"]])
    plt.legend(["Train", "Val", "Predictions"], bbox_to_anchor =(0.5,-0.27), loc = "lower right")
    plt.tight_layout()
    plt.savefig(f"plots/forecast_{unit} .png", dpi=300, transparent = True)
    plt.show()