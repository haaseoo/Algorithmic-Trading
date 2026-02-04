import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib

# 1. 맥북 전용 설정 (차트 선명도 및 한글 깨짐 방지)
plt.rcParams['figure.dpi'] = 150        # 고해상도 설정
plt.rc('font', family='AppleGothic')   # 맥북 한글 폰트 적용
plt.rcParams['axes.unicode_minus'] = False

# 2. GS 종목 데이터 받아오기
# 위키독스의 예제 기간을 최신 데이터로 대체하거나 'max'를 사용합니다.
gs = yf.download("078930.KS", start="2023-01-01")

# 3. [중요] 컬럼 이름 평탄화 (KeyError: 'Adj Close' 방지)
# (Price, Close) 형태의 구조를 'Close' 한 줄로 바꿉니다.
gs.columns = gs.columns.get_level_values(0)

# 4. 차트 그리기 (위키독스 In [19] 과정)
plt.figure(figsize=(12, 6))

# 위키독스 본문처럼 gs.index(날짜)를 X축으로, gs['Close']를 Y축으로 설정합니다.
# 최신 yfinance는 'Adj Close' 대신 'Close'에 수정 종가를 반영하기도 합니다.
plt.plot(gs.index, gs['Close'], label='GS 종가')

# 5. 차트 꾸미기
plt.title("GS 주가 추이 (기술적 분석 기초)")
plt.xlabel("날짜 (Date)")
plt.ylabel("가격 (Price)")
plt.legend(fontsize=8, loc="upper left")
plt.xticks(fontsize=8)                            # x축 눈금 숫자 크기 8
plt.yticks(fontsize=8)                            # y축 눈금 숫자 크기 8

plt.grid(True, linestyle=':', alpha=0.4)
plt.tight_layout()

# 6. 화면 출력
plt.show()