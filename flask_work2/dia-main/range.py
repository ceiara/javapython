from dataclasses import dataclass
import pandas as pd

data = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='train')

print(data.info())
print(data.describe())

print(max)
ta = data.groupby("당뇨여부").max()
print(ta)
print()

print(min)
ta = data.groupby("당뇨여부").min()
print(ta)
print()







