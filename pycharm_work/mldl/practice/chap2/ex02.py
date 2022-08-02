import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
im

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

tak = np.column_stack(([1,2,3], [4,5,6])) # 일렬로 세워 나란히 연결
print(tak)

fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data[:5])

fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)

train_input, test_input, train_target, test_target = \
    train_test_split(fish_data, fish_target, random_state=42)

print(train_input.shape, test_input.shape) # 2개의 열이 있는 2차원 데이터
print(train_target.shape, test_target.shape) # 1차원 배열
print(test_target) # 빙어 데이터 수가 너무 작아 잘 섞이지 않음
# 그래서 다시 돌림, stratify: 클래스 비율에 맞게 데이터를 나눈다.
train_input, test_input, train_target, test_target = \
    train_test_split(fish_data, fish_target, stratify=fish_target, random_state=42)
print(test_target)

# k-최접근 이웃 훈련
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
score = kn.score(test_input, test_target)
print(score)

# 산점도로 확인
plt.scatter(train_input[:, 0], train_input[:, 1]) #[행, 열), 처음부터 마지막 원소까지(시작 인덱스와 마지막 인덱스 생략 가능)
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


