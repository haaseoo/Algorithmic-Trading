import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.style as style

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

style.use('ggplot')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
labels = ['삼성전자', 'SK하이닉스', 'LG전자', '네이버', '카카오']
ratio = [50, 20, 10, 10, 10]
explode = (0.0, 0.1, 0.0, 0.0, 0.0)

plt.pie(ratio,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90)

plt.show()