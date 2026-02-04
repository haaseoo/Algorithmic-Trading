import matplotlib.pyplot as plt

# 2x2 그리드의 서브플롯 생성
fig, ax_list = plt.subplots(2, 2)

# ax_list는 2차원 배열이므로 인덱스로 접근 가능
# 오른쪽 하단(1행 1열 위치)에 그래프 그리기
ax_list[1][1].plot([1, 2, 3, 4])

plt.show()