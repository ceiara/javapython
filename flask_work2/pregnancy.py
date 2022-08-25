import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from mpl_toolkits.axes_grid1 import host_subplot

plt.style.use("ggplot")
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

plt.style.use("seaborn-deep")
data = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='train')

# ta = data.groupby('인슐린').max()
# print(ta)
# {'X':data['임신'],'Y':data['인슐린']}
imsin = data['임신'].to_numpy()
print(imsin[:5])
insul = data['인슐린'].to_numpy()
print(insul[:5])
target = data['당뇨여부'].to_numpy()
# print()

mydata1 = insul[target==1]
mydata1[mydata1 >=10]


mydata2 = insul[target==0]
mydata2[mydata2 >=10]
# 데이터 생성
# df1=pd.DataFrame()

im10highavg =np.mean(insul[imsin>=10])
im10lowavg = np.mean(insul[imsin<10])
'''
참조 https://www.amc.seoul.kr/asan/healthinfo/management/managementDetail.do?managementId=138 

원래 당뇨가 없던 사람이 임신 20주 이후에 당뇨병이 발생하는 경우를 말합니다. 
태아에서 분비되는 호르몬으로 인해 임신부의 인슐린 기능이 떨어지게 되면 정상적으로 
이를 극복하기 위해 췌장에서 인슐린 분비가 증가하게 되는데, 이때 인슐린 분비가 충분치 않을 경우 임신성 당뇨가 발생하게 됩니다

'''

print(im10highavg)
print(im10lowavg)

#그래프생성
# plt.plot(mydata1,color='red',linestyle='-',linewidth='0.5')
# plt.plot(mydata2,color='green',linestyle='-',linewidth='0.5')
# plt.plot(imsin,color='blue',linestyle='-')

# plt.plot(['x1','x2'],[im10highavg,im10lowavg])
plt.hist(insul[imsin>=10],alpha=0.8,color='red')

#그래프 정보 설정
# plt.xlim(0, 10) #x축 범위
# plt.ylim(0, 680) #y축 범위
plt.xlabel('임신') #x 라벨
plt.ylabel('인슐린') #y 라벨
plt.title("임신 중 인슐린 수치") #그래프 이름

plt.savefig('임신수치10이상.png')


# plt.hist(insul[imsin<10],alpha=0.8,color='yellow')
# plt.savefig('임신수치10미만.png')

