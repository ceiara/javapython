# 문제1
for i in list(range(9,0,-1)):
    num = 7
    num *= i
    print(num, end=' ')

print()
#문제 2
for i in (tuple(range(1,100,+1)) + tuple(range(100,0,-1))):
    print(i, end=' ')