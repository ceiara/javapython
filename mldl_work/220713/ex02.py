import numpy as np

a = [1,2,3,4,5]
npa = np.array(a)

a = a*5
npa = npa*5
print('a',a)
print('npa',npa) 

print(npa.shape) # 1차원 배열에 5개 들어가져있다

# np.random.seed(42) random한 패턴이 계속 같이 나옴
a = np.random.randint(1,100,5) #1~100에서 5개만 가져오기
print(a)
print(type(a))