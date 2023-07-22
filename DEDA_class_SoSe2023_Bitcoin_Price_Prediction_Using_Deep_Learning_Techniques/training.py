import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tools.sm_exceptions import ValueWarning, HessianInversionWarning, ConvergenceWarning
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

from data_loader import get_data
from data_visualization import exploratory_data_analysis
from data_preparation import prepare_data, load_data, split_data
from lstm import lstm_model
from testing import test_model

def train_scratch(start_year, end_year, cryptocurrency, currency, unit = "price", window_size = 80, split_size = 0.8, time_series = True, epochs = 25):
    print("1%")
    batch_size = 1
    df = get_data(start_year, end_year, cryptocurrency, currency, save = True)
    #df.to_csv("datasets/temp.csv", index = False)
    print("25%")
    #print(df.head())
    data = prepare_data(df, unit)
    print("30%")
    #print(data.head())
    exploratory_data_analysis(data, "price", True)
    print("45%")
    (X_train, y_train, scaled_data, dataset, training_data_len) = split_data(data, unit, window_size, split_size)
    print("60%")
    model = lstm_model(X_train)
    print("65%")

    model.fit(X_train, y_train, batch_size, epochs)
    print("80%")
    test_model(scaled_data, training_data_len, window_size, dataset, model, unit)
    print("100%")
    
    
    
    
def train_direct():
    pass

#train_scratch(2022, 2023, "BTC", "USD", unit = "price", window_size = 80, split_size = 0.8, time_series = True, epochs = 25)