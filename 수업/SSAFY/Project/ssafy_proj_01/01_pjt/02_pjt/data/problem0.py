import csv
import numpy as np
import pandas as pd

df = pd.read_csv('NFLX.CSV', encoding='cp949', usecols=['Date', 'Open', 'High', 'Low', 'Close'])
df.head()
print(df)