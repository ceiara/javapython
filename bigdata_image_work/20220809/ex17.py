import numpy as np

la = np.linspace(0,10,3)
print(la)

ra = np.random.randint(0,7,(1,3))
print(ra)

a1 = np.arange(0,10)
a2 = a1
print(a2)

a3 = np.array([4,3,1,2,3,1,3])
a4 = np.unique(a3) # 중복되는 숫자 배제
print(a4)
