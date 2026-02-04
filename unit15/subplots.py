import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# 1행 2열 구조의 그래프 생성
plt.subplot(1, 2, 1) # 첫 번째 구역
plt.plot(x, np.sin(x), color='blue')
plt.title('Sine Wave')

plt.subplot(1, 2, 2) # 두 번째 구역
plt.plot(x, np.cos(x), color='red')
plt.title('Cosine Wave')

plt.tight_layout() # 그래프 간격 자동 조절
plt.show()