
# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt
from prophet import Prophet

# Step 2: Load and Explore Data
# Here we use the Airline Passengers dataset.
data_url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
data = pd.read_csv(data_url, parse_dates=['Month'], index_col='Month')
print(data.head())

# Visualize the data
plt.figure(figsize=(10, 6))
plt.plot(data, label='Passenger Traffic')
plt.title('Monthly Airline Passenger Traffic')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.legend()
plt.show()
