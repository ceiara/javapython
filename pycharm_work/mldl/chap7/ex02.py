import numpy
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

(train_input, train_target),(test_input, test_target) \
    = keras.datasets.fashion_mnist.load_data()

train_scaled = train_input.reshape(-1,784)/255.0 # 255로 나누어 0~1 사이의 값으로 정규화, 양수 값으로 이루어진 이미지를 전처리할 때 사용하는 방법
test_scaled = test_input.reshape(-1,784)/255.0 # reshape - 1차원을 2차원으로 바꿈

print(train_scaled.shape)
print(test_scaled.shape)

train_scaled, val_scaled, train_target, val_target = \
    train_test_split(train_scaled,train_target, random_state=42)

dense = keras.layers.Dense(10, activation='softmax', input_shape=(784,))

model = keras.Sequential(dense)
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')

model.fit(train_scaled, train_target, epochs=5)

훈련점수 = model.evaluate(train_scaled, train_target)
print(훈련점수)

import ex03
#0티셔츠1바지2스웨터3드레스4코드5샌달6셔츠7스니커즈8가방9앵글부츠
t1 = ex03.t1()/255.0
t1 = 1 - t1 # 색상 반전: gray_r를 했을 때 원래 하얀 배경이 검은 색으로 바껴 다시 검은 배경을 하얀 배경색으로 바꿈
print()
print(t1.reshape(-1, 784))
print()
print(numpy.round(t1,decimals=3))
pred = model.predict(t1.reshape(-1, 784))
print(pred)

print(np.argmax(pred))

import matplotlib.pyplot as plt

plt.imshow(t1, cmap='gray_r')
plt.show()

sh1 = ex03.sh1()/255.0
sh1 = 1 - sh1
print(numpy.round(t1,decimals=3))
pred = model.predict(sh1.reshape(-1, 784))
print(pred)

print(np.argmax(pred))

plt.imshow(sh1, cmap='gray_r')
plt.show()

p1 = ex03.p1()/255.0
p1 = 1 - p1
print(numpy.round(p1,decimals=3))
pred = model.predict(p1.reshape(-1, 784))
print(pred)

print(np.argmax(pred))

plt.imshow(p1, cmap='gray_r')
plt.show()

sa = ex03.sa()/255.0
sa = 1 - sa
print(numpy.round(sa,decimals=3))
pred = model.predict(sa.reshape(-1, 784))
print(pred)

print(np.argmax(pred))

plt.imshow(sa, cmap='gray_r')
plt.show()