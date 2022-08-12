from matplotlib.patches import ConnectionPatch
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-ticks")
data = pd.read_excel('static/data/carprice/carprice.xlsx')

# ta = data.groupby('년식').mean()
# print(ta)
# print(type(ta))
# print(ta.columns)
# print(ta.index.to_numpy())

# plt.bar(ta.index.to_numpy()-0.1,ta['가격'].to_numpy(),width=0.1,alpha=0.5, label='price')
# plt.bar(ta.index.to_numpy(),ta['배기량'].to_numpy(),width=0.1,alpha=0.5, label='displacement')
# plt.bar(ta.index.to_numpy()+0.1,ta['중량'].to_numpy(),width=0.1,alpha=0.5, label='weight')
# plt.xticks(rotation=30)
# plt.yticks(rotation=30)
# # plt.grid()
# plt.legend()
# # plt.show()
# plt.savefig('x3_y1.png')

# ta2 = data.groupby("년식")['종류'].sum()
# print(ta2)
# str_count1 = ta2[2015].count('대형')
# str_count2 = ta2[2015].count('중형')
# str_count3 = ta2[2015].count('준준형')
# str_count4 = ta2[2015].count('소형')
# print("대형 = ",str_count1)
# print("중형 = ",str_count2)
# print("준준형 = ",str_count3)
# print("소형 = ",str_count4)

# category_names = ['대형','중형','준준형','소형']

# results = {
#     '2011': [0,0,0,4],
#     '2012': [0,0,1,3],
#     '2013': [0,0,0,3],
#     '2014': [4,0,0,2],
#     '2015': [22,28,0,4]
# }

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

overall_ratios = [.0563, .0563, .0423, .0845, .7606]
labels = ['2011', '2012', '2013', '2014', '2015']
explode = [0, 0, 0, 0, 0.1]

angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)

age_ratios = [.4074, .5185, 0, .0741]
age_labels = ['sled', 'mid-sized', 'submidsize', 'compact']
bottom = 1
width = .2

for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax2.set_title('Size of Car')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(age_ratios)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)

# plt.show()