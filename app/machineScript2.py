import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split



df = pd.read_csv('AAPL.csv', index_col="Date", parse_dates=True)
df = df[['Adj Close']]

forecast = 30
df.pre

