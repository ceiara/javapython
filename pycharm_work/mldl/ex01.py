from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_excel('data.xlsx')
length = data['length'].to_numpy()
weight = data['weight'].to_numpy()
target = data['target'].to_numpy()

data = np.column_stack((length,weight))
print(data[:5])
print(data.shape)

data5 = np.full((3,3),5)
print(data5)

train_input, test_input, train_target, test_target \
    = train_test_split(data, target, random_state=42, stratify=target)

print(train_input.shape)
print(test_input.shape)

print(train_target.shape)
print(test_target.shape)
