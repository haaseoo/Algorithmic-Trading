# 국내 주식 시세

import mojito
import pprint
import pandas as pd

with open("../secrets/koreainvestment.key", "r", encoding="utf-8") as f:
    lines = f.readlines()

    key = lines[0].strip()
    secret = lines[1].strip()
    acc_no = lines[2].strip()

    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no,
        mock=True
)

resp = broker.fetch_ohlcv(
    symbol="005930",
    timeframe="D",
    adj_price=True
)

# pprint.pprint(resp)

# 일봉 데이터 다루기 (과거 흐름 파악용)

df = pd.DataFrame(resp['output2'])

# 문자열 데이터를 숫자로 변환
df[['stck_oprc', 'stck_hgpr', 'stck_lwpr', 'stck_clpr']] = df[
    ['stck_oprc', 'stck_hgpr', 'stck_lwpr', 'stck_clpr']].apply(pd.to_numeric)

# 날짜 인덱스 설정
dt = pd.to_datetime(df['stck_bsop_date'], format='%Y%m%d')
df.set_index(dt, inplace=True)
df = df[['stck_oprc', 'stck_hgpr', 'stck_lwpr', "stck_clpr"]]
df.columns = ['open', 'high', 'low', 'close']
df.index.name = 'date'

print("----- 일봉 데이터 (최근 5일) -----")
print(df.tail())

# 당일 분봉 데이터 다루기 (실시간 매매용)
result = broker.fetch_today_1m_ohlcv("005930")

if 'output2' in result and result['output2']:
    df_min = pd.DataFrame(result['output2'])

    # 1. 숫자 데이터로 변환
    cols = ['stck_oprc', 'stck_hgpr', 'stck_lwpr', 'stck_prpr', 'cntg_vol']
    df_min[cols] = df_min[cols].apply(pd.to_numeric)

    # 2. 시간 인덱스 설정 (날짜 + 시간 합치기)
    dt_min = pd.to_datetime(df_min['stck_bsop_date'] + " " + df_min['stck_cntg_hour'], format="%Y%m%d %H%M%S")
    df_min.set_index(dt_min, inplace=True)

    # 3. 필요한 컬럼만 추출 및 이름 변경
    df_min = df_min[cols]
    df_min.columns = ['open', 'high', 'low', 'close', 'volume']
    df_min.index.name = 'datetime'

    # 4. 과거 -> 현재 순으로 정렬
    df_min = df_min[::-1]

    print("\n----- 분봉 데이터 (최근 5분) -----")
    print(df_min.tail())
else:
    print("\n----- 분봉 데이터 조회 불가 -----")
    print(f"사유: {result.get('msg1', '데이터가 없습니다.')}")
