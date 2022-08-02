from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14 # 정답: 도미-35, 빙어-14

kn = KNeighborsClassifier()

# 35를 훈련세트로 14개를 테스트세트로 사용
# 처음 35개를 지정하기 위해 index를 지정
print(fish_data[4])
print(fish_data[:5])

# train_test_split: 리스트나 배열을 비율에 맞게 훈련세트와 테스트 세트로 나누어 주고 알아서 섞어준다.
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

kn = kn.fit(train_input, train_target)
score = kn.score(test_input, test_target)
print(score)

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

print(input_arr)
print(input_arr.shape) # 49개의 샘플과 2개의 특성

np.random.seed(42) # 일정한 결과 출력
index = np.arange(49)
np.random.shuffle(index) # 무작위로 섞음

print(input_arr[[1, 3]])

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

print(input_arr[13], train_input[0])

kn = kn.fit(train_input, train_target)
score = kn.score(test_input, test_target)
print(score)

predict = kn.predict(test_input)
print(predict)
print(test_target)