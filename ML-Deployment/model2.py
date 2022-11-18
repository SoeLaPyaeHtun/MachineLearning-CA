import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('AMZN.csv', index_col=0, parse_dates=True , infer_datetime_format=True)

first_date = df.index[0]

RECENT_PERIOD = 50
df.ClosingPrice[-RECENT_PERIOD:]
df_recent_period = df[-RECENT_PERIOD:]

RECENT_PERIOD1 = 200
df.ClosingPrice[-RECENT_PERIOD1:]
df_recent_period1 = df[-RECENT_PERIOD1:]

df_recent_period.ClosingPrice.mean()
df_recent_period.ClosingPrice.sum()
rolling_mean_50 = df.ClosingPrice.rolling(window=50).mean().shift(1)
rolling_mean_200 = df.ClosingPrice.rolling(window=200).mean().shift(1)


rolling_mean_50.to_pickle('model2.pkl')
rolling_mean_200.to_pickle('model21.pkl')