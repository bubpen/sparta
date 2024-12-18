import numpy as np
import pandas as pd
print()
data_csv = pd.read_csv('housingdata.csv')
print(data_csv.isna().sum(), data_csv.dtypes)
data_csv_median = data_csv.fillna(data_csv.median)
print(data_csv_median)