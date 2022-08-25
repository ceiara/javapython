from tensorflow import keras
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 데이터 전처리
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input.reshape(-1, 28, 28, 1) / 255.0 

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# 모델 만들기
model = keras.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(28,28,1)))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Conv2D(64, kernel_size=(3,3), activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()

# 모델 학습하기
keras.utils.plot_model(model)
keras.utils.plot_model(model, show_shapes=True, to_file='cnn-architecture.png', dpi=100) # 모델 만드는 과정 보여쥼, dpi:해상도

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy') # adam 알고리즘으로 학습

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5', save_best_only=True)
# ModelCheckpoint: 조건을 만족했을 때 Model의 weight 값을 중간 저장
# 20번 학습한 것 중에 best의 위치을 알려줌, best-cnn-model.h5으로 저장
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,restore_best_weights=True)
# best에 도달하고 2번 정도 더 출력하고 멈춤

history = model.fit(train_scaled, train_target, epochs=20,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])
