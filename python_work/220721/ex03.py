import copy

a = [10,20,30,40,(50,60),[10,20,30]]
b = a # 변수 선언 b와 a는 같은 공간 공유

a[-1]=[555,666]

print(a)
print(b)
print("카피하기전에 ....")

c = copy.copy(a) # a를 복사한 새로운 c 생성
a[-1]=[888,999]

print(a)
print(c)

a[-2]=(333,444)
print(a)
print(c)

