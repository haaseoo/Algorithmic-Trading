import pandas as pd
import yfinance as yf
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

# Zipline 관련 임포트
from zipline.api import order_target, record, symbol
from zipline.algorithm import TradingAlgorithm
from zipline.finance.trading import TradingEnvironment
from zipline.utils.factory import create_simulation_parameters

# 1. 데이터 준비
start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
end = datetime(2016, 3, 29, 0, 0, 0, 0, pytz.utc)

data = yf.download("AAPL", start=start, end=end)
data = data[['Close']].copy()
data.columns = ['AAPL']
data.index = data.index.tz_localize("UTC") if data.index.tz is None else data.index.tz_convert("UTC")

# 2. 알고리즘 함수 정의
def initialize(context):
    context.i = 0
    context.sym = symbol('AAPL')

def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return

    ma5 = data.history(context.sym, 'price', 5, '1d').mean()
    ma20 = data.history(context.sym, 'price', 20, '1d').mean()

    if ma5 > ma20:
        order_target(context.sym, 1)
    else:
        order_target(context.sym, -1)

    record(AAPL=data.current(context.sym, "price"), ma5=ma5, ma20=ma20)

# 3. 백테스트 실행 (sim_params 추가)
# TradingAlgorithm은 데이터와 연동된 시뮬레이션 파라미터를 필요로 합니다.
algo = TradingAlgorithm(
    initialize=initialize,
    handle_data=handle_data,
    identifiers=['AAPL']  # 사용할 심볼 명시
)

# run 메서드 호출 시 데이터를 직접 전달합니다.
result = algo.run(data)

# 4. 결과 출력
print(result[['portfolio_value', 'ma5', 'ma20']].tail())
result[['ma5', 'ma20']].plot()
plt.show()