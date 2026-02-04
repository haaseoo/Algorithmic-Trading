import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 'ro--' : r(빨간색), o(원형 마커), --(파선)
plt.plot(x, y, 'ro--', linewidth=2, markersize=8)

plt.title('Styled Plot')
plt.grid(True) # 격자 추가
plt.show()