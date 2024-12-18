import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('housingdata.csv')
print(df)
df_median = df[:]

# 결측치를 평균값으로 대체, CHAS 는 0 과 1로 구분되어 0으로 대체
for i in df_median.columns:
    if df_median[i].isnull().sum() > 0:
        if i == 'CHAS':
            df_median[i] = df_median[i].fillna(0)
        else:
            df_median[i] = df_median[i].fillna(df[i].mean())



X = df_median[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']]
y = df_median['MEDV']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

# 다항 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')



# df_without_na = df.dropna()
# df_without_na.to_csv('data_csv_no_na.csv',index ='False')