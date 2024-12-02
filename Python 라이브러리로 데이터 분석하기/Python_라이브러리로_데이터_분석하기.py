import pandas as pd
import numpy as np
# 기본문제
# 3 - 1. Python 라이브러리 함수를 사용하여 엑셀 파일을 불러오고, DataFrame을 출력해주세요.
# 설치한 데이터를 불러오기.
df_xlsx = pd.read_excel('관서별 5대범죄 발생 및 검거.xlsx')

print(df_xlsx)

# 3 - 2. 각 경찰서(`관서명`)를 해당 구 이름으로 매핑하여 '구별'이라는 새로운 column을 생성하고, DataFrame을 출력해주세요.
#    - 매칭되지 않는 경찰서명에 대해서는 기본값 `'구 없음'`을 할당합니다.
p_appliation = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
'서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
'혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
'마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
'광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
'강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
'구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
'방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}

# 소재지를 관서명에 매핑
df_xlsx['구별'] = df_xlsx['관서명'].map(p_appliation)

# 계의 '구별'이 none이이에 '구 없음'으로 채움.
df_xlsx['구별'] = df_xlsx['구별'].fillna('구 없음')
print(df_xlsx)

# 3 - 3. `pivot_table` 을 사용하여 관서별 데이터를 구별 데이터로 변경하고, 같은 구의 경우에는 sum을 적용하여 더해주세요. (index : 관서명 -> 구별)

# 쓸 열들만 모와서 따로 정리
pivot_df = df_xlsx[['구별', '강간(검거)', '강간(발생)', '강도(검거)', '강도(발생)', '살인(검거)', '살인(발생)', '소계(검거)', '소계(발생)', '절도(검거)', '절도(발생)', '폭력(검거)', '폭력(발생)']]
# pivot_table 생성
pivot_df = pivot_df.pivot_table(index = '구별', aggfunc = 'sum')
print(pivot_df)

# 3-4. '구 없음'  행은 drop 을 활용하여 삭제해주세요.
pivot_df.drop(['구 없음'])

# 3- 5. 각 범죄 별로 검거율을 계산하고, 각 검거율 데이터 column을 DataFrame에 추가해주세요.
# 검거율의 컬럼들을 생성해주고, 그 값들은 기존 컬럼을 이용해 값을 생성
pivot_df['강간검거율'] = pivot_df['강간(검거)']/pivot_df['강간(발생)'] * 100
pivot_df['강도검거율'] = pivot_df['강도(검거)']/pivot_df['강도(발생)'] * 100
pivot_df['살인검거율'] = pivot_df['살인(검거)']/pivot_df['살인(발생)'] * 100
pivot_df['절도검거율'] = pivot_df['절도(검거)']/pivot_df['절도(발생)'] * 100
pivot_df['폭력검거율'] = pivot_df['폭력(검거)']/pivot_df['폭력(발생)'] * 100
pivot_df['검거율'] = pivot_df['소계(검거)']/pivot_df['소계(발생)'] * 100
pivot_df

# 3- 6. 필요없는 column을 del 을 사용하여 삭제해주세요.
# del '데이터프레임'['컬럼명'] 으로 컬럼을 삭제
del pivot_df['강간(검거)']
del pivot_df['강도(검거)']
del pivot_df['살인(검거)']
del pivot_df['절도(검거)']
del pivot_df['폭력(검거)']
del pivot_df['소계(발생)']
del pivot_df['소계(검거)']

pivot_df

# 3 - 7. DataFrame의 컬럼명을 rename 을 사용하여 변경해주세요.
pivot_df = pivot_df.rename(columns = {'강간(발생)':'강간'})
pivot_df = pivot_df.rename(columns = {'강도(발생)':'강도'})
pivot_df = pivot_df.rename(columns = {'살인(발생)':'살인'})
pivot_df = pivot_df.rename(columns = {'절도(발생)':'절도'})
pivot_df = pivot_df.rename(columns = {'폭력(발생)':'폭력'})
pivot_df = pivot_df.rename(columns = {'강간(발생)':'강간', '강도(발생)':'강도', '살인(발생)':'살인', '절도(발생)':'절도', '폭력(발생)':'폭력'})
pivot_df



# 도전문제
# csv 파일이기에 read_csv 사용
df_csv = pd.read_csv("pop_kor.csv",index_col='구별')
# 이전 문제에서 생성된 데이터프레임과 '구별' 컬럼을 기준으로 병합
df_merged = pd.merge(pivot_df,df_csv, on = '구별')
# 병합된 데이터프레임을 '검거율' 컬럼을 기준으로 오름차순 정렬
df_merged = df_merged.sort_values('검거율',ascending = True)
# 호출
df_merged
