import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold

data = pd.read_csv('wine.csv')
print(data.head())

x = data[['alcohol', 'sugar', 'pH']].to_numpy()
y = data[['class']].to_numpy()

train_input, test_input, train_target, test_target \
    = train_test_split(x, y, test_size=0.2, random_state=42)

# 훈련세트: sub_input, sub_target / 검증세트: val_input, val_target
sub_input, val_input, sub_target, val_target \
    = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

print(sub_input.shape)
print(val_input.shape)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))

score = cross_validate(dt, train_input, train_target)
print(score)

print(np.mean(score['test_score']))

scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())
print(np.mean(scores['test_score']))

splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))

