# 국내 주식 시세

import mojito
import pprint
import pandas as pd

with open("secrets/koreainvestment.key", "r", encoding="utf-8") as f:
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

# 일봉 데이터 다루기
df = pd.DataFrame(resp['output2'])
dt = pd.to_datetime(df['stck_bsop_date'], format='%Y%m%d')
df.set_index(dt, inplace=True)
df = df[['stck_oprc', 'stck_hgpr', 'stck_lwpr', "stck_clpr"]]
df.columns = ['open', 'high', 'low', 'close']
df.index.name = 'date'
# print(df)

# 당일 분봉 데이터 조회
result = broker.fetch_today_1m_ohlcv("005930")
df = pd.DataFrame(result['output2'])
dt = pd.to_datetime(df['stck_bsop_date'] + " " + df['stck_cntg_hour'], format="%Y%m%d %H%M%S")
df.set_index(dt, inplace=True)
df = df[['stcl_oprc', 'stck_hgpr', 'stck_lwpr', 'stck_prpr', 'cntg_vol']]
df.columns = ['open', 'high', 'low', 'close', 'volume']
df.index.name = 'datetime'
df = df[::-1]
print(df)