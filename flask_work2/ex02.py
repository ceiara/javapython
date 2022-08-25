import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.style.use("seaborn-deep")
data = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='train')


print("mean")
ta = data.groupby("당뇨여부").mean()
print(ta)

plt.style.use("ggplot")
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

labels = ['글루코스', '인슐린', '혈압', 'BMI', '나이', '가족력']
bad = [140.8, 136.6, 75.0, 35.9, 36, 0.6]
good = [108.4, 93.4, 69.9, 31.6, 29, 0.4]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, bad, width, label='비정상')
rects2 = ax.bar(x + width/2, good, width, label='정상')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('평균')
ax.set_title('당뇨 여부에 따른 평균 수치')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

# plt.show()
plt.savefig('mean.png')





