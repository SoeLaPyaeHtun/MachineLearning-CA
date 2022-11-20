import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('AMZN.csv', index_col=0, parse_dates=True , infer_datetime_format=True)
print(df.dtypes)

first_date = df.index[0]
first_date

RECENT_PERIOD = 50
df.ClosingPrice[-RECENT_PERIOD:]
df_recent_period = df[-RECENT_PERIOD:]

df_recent_period.ClosingPrice.mean()
df_recent_period.ClosingPrice.sum()

rolling_mean_50 = df.ClosingPrice.rolling(window=50).mean().shift(1)
rolling_mean_200 = df.ClosingPrice.rolling(window=200).mean().shift(1)

print(df.ClosingPrice.head())
print("-----rolling mean 50-----")
print(rolling_mean_50.head())
print("-----rolling mean 200-----")
print(rolling_mean_200.head())

plt.plot(df.index, df.ClosingPrice, label='Closing Price')
plt.plot(df.index, rolling_mean_50, label='Closing Price 50 Days SMA', color='orange')
plt.plot(df.index, rolling_mean_200, label='Closing Price 200 Days SMA', color='magenta')
plt.legend(loc='upper left')
plt.show()

rolling_mean_50.to_pickle('model2.pkl')
