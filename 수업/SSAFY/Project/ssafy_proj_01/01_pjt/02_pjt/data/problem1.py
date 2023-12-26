import csv
import numpy as np
import pandas as pd

def file_open_by_numpy():
    # np.loadtxt(구분자 = ',', 데이터 타입: string)
    np_arr = np.loadtxt('NFLX.CSV', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

arr = file_open_by_numpy()

columns=arr[0]
arr = np.delete(arr, 0, 0)
df = pd.DataFrame(arr, columns=columns)


df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
print(df)