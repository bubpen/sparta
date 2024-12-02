import pandas as pd
import numpy as np
# 3 - 1 
df_csv = pd.read_csv('pop_kor.csv')
df_xlsx = pd.read_excel('관서별 5대범죄 발생 및 검거.xlsx')

print(df_xlsx)

# 3 - 2
p_appliation = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
'서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
'혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
'마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
'광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
'강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
'구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
'방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}
df_app = pd.DataFrame(list(p_appliation.items()), columns = ['관서명', '구별'])
merged_df = pd.merge(df_xlsx, df_app, on = '관서명', how = 'left')
merged_df['구별'] = merged_df['구별'].fillna('구 없음')
print(merged_df)

# 3 - 3
pivot_df = pd.pivot(merged_df, index = '구별', columns = ['살인(발생)', '살인(검거)', '강도(발생)', '강도(검거)', '강간(발생)', '강간(검거)', '절도(발생)', '절도(검거)', '폭력(발생)', '폭력(검거)'], aggfunc = 'sum')
print(pivot_df)