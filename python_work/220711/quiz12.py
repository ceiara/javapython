# 문제 1 
from pandas import read_pickle


dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
dc['홈런볼'] = 900
print(dc)

print()
# 문제 2
for i in dc:
    dc[i] += 100
print(dc)

print()
# 문제 3
del dc['콘치즈']
dc['치즈콘'] = 950
print(dc)
