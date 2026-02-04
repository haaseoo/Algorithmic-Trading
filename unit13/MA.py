import yfinance as yf
import pandas as pd

# 1. 데이터 다운로드 (GS 종목코드: 078930.KS)
# pandas_datareader 대신 yfinance를 사용합니다.
gs = yf.download("078930.KS", start="2024-01-01", end="2026-02-01")

# 2. 거래량이 0인 날(공휴일) 제거
# 텍스트에서 강조한 "데이터 정제" 단계입니다.
new_gs = gs[gs['Volume'] != 0].copy()

# 3. 이동평균선(MA) 계산
# 수정 종가(Adj Close)를 기준으로 계산합니다.
new_gs['MA5'] = new_gs['Adj Close'].rolling(window=5).mean()
new_gs['MA20'] = new_gs['Adj Close'].rolling(window=20).mean()
new_gs['MA60'] = new_gs['Adj Close'].rolling(window=60).mean()
new_gs['MA120'] = new_gs['Adj Close'].rolling(window=120).mean()

# 4. 결과 확인
print(new_gs.tail(10))