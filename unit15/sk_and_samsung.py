import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import yfinance as yf

# 한글 폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 기간 설정
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2026, 2, 4)

# 데이터 다운로드
hynix = yf.download("000660.KS", start=start, end=end)
samsung = yf.download("005930.KS", start=start, end=end)

# 그래프 그리기
plt.plot(hynix.index, hynix['Close'], label='SK하이닉스')
plt.plot(samsung.index, samsung['Close'], label='삼성전자')

# 범례 및 그리드 설정
plt.legend(loc='upper left')
plt.grid(True, axis='y', color='gray', linestyle='--', alpha=0.5)

# 그래프 표시
plt.show()