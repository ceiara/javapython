# p.181 문제 1번
for i in range(9,0,-1):
    print(i*7,end=" ")

print()
# 문제 2번
a = [i for i in range(1,101)]
a = tuple(a)
b = [i for i in range(99,0,-1)]
b = tuple(b)
c = a+b
print(c)

import numpy as np
from sympy import randMatrix
 
a = np.arange(1,10)
print(list[a])

a = [i for i in range(1,10)]
print(a)

# p.187 10-1
for i in range(3):
    print(i,i+1,i+2)
print()
for i in range(3):
    print(i+1,i+2,i+3)