import numpy as np
from sklearn.cluster import KMeans # target 값 필요x
from sklearn.linear_model import LogisticRegression # target값을 정해줘야함

import matplotlib.pyplot as plt # 그래프 특화
import cv2 # 이미지 파일 특화

fruits = np.load('fruits_300.npy')
print(fruits.shape)
fruits2d = fruits.reshape(-1, 10000) # 2차원 데이터로 변경


plt.axis('off')
plt.imshow(fruits[0], cmap='gray_r')
plt.savefig('pltfruits0.png')

cv2.imwrite('cvfruits0.jpg',fruits[105])

km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits2d) # 비지도학습

predvalue = km.predict([fruits2d[0]])
print(predvalue)

a = cv2.imread('cvfruits0.jpg', cv2.IMREAD_GRAYSCALE)
print(a.shape)

pred = km.predict(a.reshape(-1, 10000))
print(pred)

target = np.array(['사과']*100 + ['파인애플']*100 + ['바나나']*100)
print(target.shape) # 300개의 일차원 데이터
print(target[:5])
print(target[100:105])
print(target[200:205])

lr = LogisticRegression()
lr.fit(fruits2d, target)

pred = lr.predict(fruits2d[0].reshape(-1, 10000)) # 1개의 행에 만개의 데이터 존재
print(pred)
pred = lr.predict(fruits2d[100].reshape(-1, 10000))
print(pred)
pred = lr.predict(fruits2d[200].reshape(-1, 10000))
print(pred)

pred = lr.predict(a.reshape(-1, 10000))
print(pred)