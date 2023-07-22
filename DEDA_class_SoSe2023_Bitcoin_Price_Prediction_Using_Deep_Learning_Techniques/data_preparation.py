import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def load_data(filename):
    df = pd.read_csv(f"datasets/{filename}")
    return df

def prepare_data(df, unit):
    df["Close time"] = pd.to_datetime(df["Close time"], unit = "ns")
    df["Close time"] = df["Close time"].dt.date
    df["Close"] = df["Close"].astype("float32")
    df = df.set_index(df["Close time"])
    if unit == "returns":
        data = df["Close"].pct_change().dropna().values
    else:
        data = df.filter(["Close"])
    return data

def normalize_data(dataset):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(dataset)
    return scaled_data

def split_data(data, unit, window_size = 80, train_ratio = 0.8):
    dataset = data.values
    # Get the number of rows to train the model
    training_data_len = math.ceil(len(dataset) * train_ratio)
    
    scaled_data = normalize_data(dataset)
    
    num_features = window_size
    # Create the scaled training dataset
    train_data = scaled_data[0: training_data_len, :]
    # Split the data into train and test sets
    X_train = []
    y_train = []

    for i in range(num_features, len(train_data)):
        X_train.append(train_data[i - num_features:i, 0])
        y_train.append(train_data[i, 0])
        #if i <= num_features:
        #    print(f"X_train = {X_train}, y_train = {y_train}")
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    split_plot(data, unit, training_data_len)
    return X_train, y_train, scaled_data, dataset, training_data_len

def split_plot(data, unit, training_data_len):
    train = data[:training_data_len]
    valid = data[training_data_len:]
    
    plt.figure(figsize = (16, 8))
    plt.title("Splitting the data")
    plt.xlabel("Date", fontsize = 18)
    plt.ylabel(f"BitCoin's Close {unit}", fontsize = 18)
    plt.plot(train["Close"])
    plt.plot(valid[["Close"]])
    plt.legend(["Train", "Test"], loc = "lower right")
    plt.savefig(f"plots/{unit}_split.png", dpi=300, transparent = True)
    plt.show()
    