import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from scipy.special import expit
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('https://bit.ly/fish_csv_data')
data.to_excel('fish_data.xlsx')

print(data.head())

# pandas에 numpy를 바로 사용하면 에러발생 그래서 이차원 데이터[[]]로 사용해야함
fish_data = data[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
print(fish_data[:5])
fish_target = data['Species'].to_numpy()
print(fish_target[:5])

train_input, test_input, train_target, test_target \
    = train_test_split(fish_data,fish_target,random_state=42)

ss = StandardScaler()
ss.fit(train_input) # 학습

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

print(train_scaled[:5])
print(train_target[:5])
print(test_scaled[:5])
print(test_target[:5])

knclf = KNeighborsClassifier(n_neighbors=3) #학습기 선언 - 이웃하는 좌표만
knclf.fit(train_scaled, train_target)

예측값 = knclf.predict(test_scaled)
print(예측값[:5])
print(test_target[:5])

# bream 데이터를 표준데이터로 바꿈
pre = [[242., 25.4, 30., 11.52, 4.02], [363., 29., 33.5, 12.73, 4.4555]]
pre_scaled = ss.transform(pre)

print(pre_scaled)
pre_value = knclf.predict(pre_scaled)
print(pre_value) # bream 데이터 출력

score = knclf.score(test_scaled,test_target)
print(score) # 85%의 정확률을 가짐

z = np.arange(-5, 5, 0.1)
phi = 1 / (1+np.exp(-z))
print(z)
print(phi)

plt.plot(z, phi)
plt.show()

indexs = (train_target == 'Bream')|(train_target == 'Smelt')
print(indexs)
도미빙어데이터 = train_scaled[indexs]
도미빙어타겟 = train_target[indexs]

print(도미빙어데이터.shape)
print(도미빙어타겟.shape)

lr = LogisticRegression()
lr.fit(도미빙어데이터, 도미빙어타겟) # 학습

score = lr.score(도미빙어데이터, 도미빙어타겟)
print(score)

indexs = (test_target == 'Bream')|(test_target == 'Smelt')
도미빙어데이터 = test_scaled[indexs]
도미빙어타겟 = test_target[indexs]

score = lr.score(도미빙어데이터, 도미빙어타겟)
print(score)

pre = [[242., 25.4, 30., 11.52, 4.02], [363., 29., 33.5, 12.73, 4.4555]]
pre_scaled = ss.transform(pre)

pre_value = lr.predict(pre_scaled)
print(pre_value)

z = lr.decision_function(도미빙어데이터)
print(z)

phi = 1/(1/np.exp(-z))
print(phi)

phi = expit(z)
print(phi)

훈련데이터점수리스트 = []
테스트데이터점수리스트 = []

# whitefish 데이터 양이 너무 적어 정확도가 떨어진다.
# 그래서 같은 데이터라도 그 양을 늘려 데이터를 예측한다.
# max_iter로 반복 횟수를 지정, 기본값: 100
# 규제를 제어하는 매개변수 C사용, 작을수록 규제가 커짐, 기본값: 1
for i in range(1, 100):
    lr = LogisticRegression(C=i, max_iter=1000) # C: 규제의 강도
    lr.fit(train_scaled, train_target)

    훈련데이터점수 = lr.score(train_scaled,train_target)
    테스트데이터점수 = lr.score(test_scaled, test_target)

    훈련데이터점수리스트.append(훈련데이터점수)
    테스트데이터점수리스트.append(테스트데이터점수)

print(훈련데이터점수리스트)
print(테스트데이터점수리스트)
print(np.argmax(훈련데이터점수리스트)) # 요소 몇 번째가 가장 큰 값인가
print(np.argmax(테스트데이터점수리스트))

plt.plot(range(1, 100), 훈련데이터점수리스트)
plt.plot(range(1, 100), 테스트데이터점수리스트)
plt.show()

pre = [[242., 25.4, 30., 11.52, 4.02], [363., 29., 33.5, 12.73, 4.4555], [1000, 40, 43.5, 12.354, 6.525]]
pre_scaled = ss.transform(pre)

pre_value = lr.predict(pre_scaled)
print(pre_value)
# whitefish 알고리즘을 알지 못 함






