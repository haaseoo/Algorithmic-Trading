import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import pytz

# 1. 날짜 설정 (위키독스 예제와 동일)
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)

# 2. 데이터 다운로드
data = yf.download("AAPL", start=start, end=end)

# 3. 데이터 구조 평탄화 (최신 yfinance의 이중 컬럼 해제)
data.columns = data.columns.get_level_values(0)

# 4. 그래프 확인 (출력 결과에 따라 'Close' 사용)
plt.plot(data.index, data['Close'])
plt.show()