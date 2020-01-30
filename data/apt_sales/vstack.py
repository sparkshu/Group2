import numpy as np
import pandas as pd

all_csv = ['아파트(매매)__실거래가_201901.csv', '아파트(매매)__실거래가_201902.csv', '아파트(매매)__실거래가_201903.csv', '아파트(매매)__실거래가_201904.csv', '아파트(매매)__실거래가_201905.csv', '아파트(매매)__실거래가_201906.csv', '아파트(매매)__실거래가_201907.csv', '아파트(매매)__실거래가_201908.csv', '아파트(매매)__실거래가_201909.csv', '아파트(매매)__실거래가_201910.csv', '아파트(매매)__실거래가_201911.csv', '아파트(매매)__실거래가_201912.csv']

all_data =['data01', 'data02', 'data03', 'data04', 'data05', 'data06', 'data07', 'data08', 'data09', 'data10','data11', 'data12']  

for index, name in all_csv:
    all_data[i] = pd.read_csv(name, encoding='cp949')
# data01 = pd.read_csv('아파트(매매)__실거래가_201901.csv', encoding='cp949')
# data02 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201902.csv', encoding='cp949')
# data03 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201903.csv', encoding='cp949')
# data04 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201904.csv', encoding='cp949')
# data05 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201905.csv', encoding='cp949')
# data06 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201906.csv', encoding='cp949')
# data07 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201907.csv', encoding='cp949')
# data08 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201908.csv', encoding='cp949')
# data09 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201909.csv', encoding='cp949')
# data10 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201910.csv', encoding='cp949')
# data11 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201911.csv', encoding='cp949')
# data12 = pd.read_csv('data/apt_sales/아파트(매매)__실거래가_201912.csv', encoding='cp949')

np_data_01 = np.asarray(data01)
np_data_02 = np.asarray(data02)
np_data_03 = np.asarray(data03)
np_data_04 = np.asarray(data04)
np_data_05 = np.asarray(data05)
np_data_06 = np.asarray(data06)
np_data_07 = np.asarray(data07)
np_data_08 = np.asarray(data08)
np_data_09 = np.asarray(data09)
np_data_10 = np.asarray(data10)
np_data_11 = np.asarray(data11)
np_data_12 = np.asarray(data12)

sales_combined = np.vstack([np_data_01, np_data_02, np_data_03, np_data_04, np_data_05, np_data_06, np_data_07, np_data_08, np_data_09, np_data_10, np_data_11, np_data_12])

sales_combined = pd.DataFrame(sales_combined)

sales_combined.to_csv('C:/Users/PIRL/Desktop/apt_sales_2019.csv', encoding='cp949')