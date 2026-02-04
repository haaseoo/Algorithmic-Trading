import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import mpl_finance
import matplotlib.ticker as ticker
import numpy as np

# 1. 맥북 한글 폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 2. 데이터 가져오기
start = datetime.datetime(2026, 1, 1)
end = datetime.datetime(2026, 1, 31)
df = yf.download("000660.KS", start=start, end=end)

# 3. 데이터 정제 (휴장일 제거)
df = df[df['Volume'] > 0].copy()

# 4. 변수 정의
opens = df['Open'].values.flatten()
highs = df['High'].values.flatten()
lows = df['Low'].values.flatten()
closes = df['Close'].values.flatten()

# 5. 차트 생성 및 레이아웃 설정
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# 6. x축 눈금(Ticker) 설정: 월요일만 추출하여 날짜 표시
day_list = []
name_list = []
for i, day in enumerate(df.index):
    if day.dayofweek == 0:  # 월요일
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d') + '(Mon)')

ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

# 7. 봉 차트 그리기
mpl_finance.candlestick2_ohlc(ax, opens, highs, lows, closes,
                              width=0.5, colorup='r', colordown='b')

# 8. 최종 출력
plt.title("SK하이닉스 봉 차트")
plt.grid(True, alpha=0.3)
plt.show()