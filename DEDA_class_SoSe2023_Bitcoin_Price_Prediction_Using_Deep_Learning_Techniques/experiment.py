import pandas as pd
from data_preparation import prepare_data
from data_visualization import exploratory_data_analysis
df = pd.read_csv("datasets/temp.csv")
data = prepare_data(df, "price")
exploratory_data_analysis(data, "price", True)