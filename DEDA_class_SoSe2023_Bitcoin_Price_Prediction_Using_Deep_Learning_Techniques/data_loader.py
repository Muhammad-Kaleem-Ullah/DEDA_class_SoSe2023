import requests
import json
import pandas as pd
from datetime import datetime

def get_data(start_year, end_year, cryptocurrency, currency, save = True):
    
    
    """
        Parameters:
                    start_year:         extract data from the year
                    end_year:           extract until this year
                    cryptocurrency:     short name of Cryptocurrency whose data is meant to be extracted (i.e. BTC for Bitcoin)
                    currency:           short name of currency whose data is meant to be extracted (i.e. USD for US Dollar)
                    save:               True to save the data in a folder called "datasets"
    """
    
    years = {}
    for i in range(start_year, end_year + 1):
        if i < 2018 or i > datetime.now().year:
            print("The year ", i, " is skipped as either it is not in the range(2018,", datetime.now().year, ")")
        else:
            if i == datetime.now().year:
                years[i] = {"start_date": datetime(i, 1, 1), "end_date": datetime.now()}
                continue
            years[i] = {"start_date": datetime(i, 1, 1), "end_date": datetime(i + 1, 1, 1)}
    df = pd.DataFrame()
    temp_df = pd.DataFrame()
    for year in years.keys():
        # Set the parameters for the API request
        symbol = f"{cryptocurrency}{currency}T"  # Trading pair symbol
        interval = '1d'  # Daily interval
        start_date = years[year]["start_date"]
        end_date = years[year]["end_date"]
        start_time = int(start_date.timestamp() * 1000)  # Start time in milliseconds
        end_time = int(end_date.timestamp() * 1000)  # End time in milliseconds (current timestamp)
        # Define the API endpoint URL
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}"
        # Send the API request
        response = requests.get(url)
        data = json.loads(response.text)
        # Process the response data
        columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                   'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
        if df.empty:
            df = pd.DataFrame(data, columns=columns)
        else:
            temp_df = pd.DataFrame(data, columns=columns)
            df = pd.concat([df, temp_df], axis = 0)
    # Convert timestamps to datetime format
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
    df = df[df["Close"].notnull()]
    if save:
        import os
        if not os.path.exists("datasets"):
            os.makedirs("datasets")
        if os.path.exists(f"datasets/{cryptocurrency.lower()}{currency.lower()}t.csv"):
            print("True")
            c = 0
            while os.path.exists(f"datasets/{cryptocurrency.lower()}{currency.lower()}t{c}.csv"):
                c = c + 1
            df.to_csv(f"datasets/{cryptocurrency.lower()}{currency.lower()}t{c}.csv", index = False)
        else:
            df.to_csv(f"datasets/{cryptocurrency.lower()}{currency.lower()}t.csv", index = False)
    return df