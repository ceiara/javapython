import numpy as np
from tensorflow import keras
from sklearn.model_selection import train_test_split
import ex03

(train_input, train_target), (test_input, test_target) \
    = keras.datasets.fashion_mnist.load_data()

train_input, val_input, train_target, val_target = \
    train_test_split(train_input, train_target, random_state=42)

train_scaled = train_input/255.0
test_scaled = test_input/255.0
val_scaled = val_input/255.0

model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28))) #Flatten이 자동으로 2차원으로 변경하기 때문에 reshape할 필요x
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy', optimizer='sgd')

model.fit(train_scaled, train_target,epochs=7)

훈련점수 = model.evaluate(train_scaled, train_target)
print(훈련점수)

gabang = 1-ex03.gabang()
p1 = 1 - ex03.p1()
sa = 1 - ex03.sa()
sh1 = 1 - ex03.sh1()
t1 = 1 - ex03.t1()

pred = model.predict(gabang.reshape(-1, 28, 28)) # 한개의 이미지가 3차원으로
print(np.round(pred,decimals=0))
print(np.argmax(pred))

pred = model.predict(p1.reshape(-1, 28, 28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))

pred = model.predict(sa.reshape(-1, 28, 28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))

pred = model.predict(sh1.reshape(-1, 28, 28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))

pred = model.predict(t1.reshape(-1, 28, 28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))
