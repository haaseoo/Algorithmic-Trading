import matplotlib.pyplot as plt
import yfinance as yf

# 1. 데이터 가져오기
df = yf.download("000660.KS", start="2016-01-01", end="2026-01-31")

# 2. 맥북 한글 폰트 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 3. Figure 및 GridSpec 설정 (4행 1열 구조)
fig = plt.figure(figsize=(12, 8))
gs = fig.add_gridspec(4, 1) # 전체를 4행으로 나눔

# 4. 서브플롯 배치
# 상단 차트 (0번행부터 3번행 직전 3칸 차지)
ax_price = fig.add_subplot(gs[0:3, 0])
# 하단 차트 (마지막 3번행 1칸 차지)
ax_volume = fig.add_subplot(gs[3, 0])

# 5. 그래프 그리기
ax_price.plot(df.index, df['Close'], color='blue', linewidth=1)
ax_volume.plot(df.index, df['Volume'], color='blue', linewidth=1)

# 6. 세부 설정
ax_volume.get_yaxis().get_major_formatter().set_scientific(False)

# x축 범위 통일
ax_price.set_xlim(df.index[0], df.index[-1])
ax_volume.set_xlim(df.index[0], df.index[-1])

plt.tight_layout()
plt.show()