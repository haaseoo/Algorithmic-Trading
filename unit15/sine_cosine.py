import numpy as np
import matplotlib.pyplot as plt

# 0부터 2π까지 0.1 간격으로 배열 생성
x = np.arange(0.0, 2 * np.pi, 0.1)

# 데이터 계산
sin_y = np.sin(x)
cos_y = np.cos(x)

# 그래프 그리기 (Figure 객체 생성)
fig = plt.figure()

# 첫 번째 서브플롯 (2행 1열의 1번)
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x, sin_y, 'b--')  # 파란색 점선

# 두 번째 서브플롯 (2행 1열의 2번)
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, cos_y, 'r--')  # 빨간색 점선

# 그래프 표시
plt.show()