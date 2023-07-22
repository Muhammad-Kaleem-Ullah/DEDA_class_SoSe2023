import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import plot_model


def lstm_model(X_train):
    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences = True, input_shape = (X_train.shape[1], 1), name = "LSTM_layer1"))
    model.add(LSTM(50, return_sequences = False, name = "LSTM_layer2"))
    model.add(Dense(25))
    model.add(Dense(1))
    print(model.summary())
    model.compile(optimizer = "adam", loss = "mean_squared_error")
    return model