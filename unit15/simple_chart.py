import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y, label='Linear')

# 제목 및 축 이름 설정
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 범례 표시
plt.legend()

# 그래프 출력
plt.show()