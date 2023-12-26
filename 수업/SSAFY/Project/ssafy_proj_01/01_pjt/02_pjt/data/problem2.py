import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('NFLX.CSV', encoding='cp949', usecols=['Date', 'Open', 'High', 'Low', 'Close'])
df.head()
print(df)


# df['Date'] = df['Date'].astype('datetime64[ns]')
df['Date'] = pd.to_datetime(df['Date'])
df.dtypes

df_2021=df[df['Date'] >= '2021.01.01']
# filtered_df=df.loc[df_2021]

# 데이터 생성

y=[df['Close']]
x=[df['Date']]

# 그래프 그리기
plt.plot(x,y)

# 그래프에 제목과 축 레이블 추가
plt.title('NFLX Close Price')
plt.ylabel('Close Price')
plt.xlabel('Date')

# 그래프 표시
plt.show()