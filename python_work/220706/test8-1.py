# 문제 1
num = 0
while num <10:
    print("num =",num)
    num +=1
print()
# 문제 2
num = 9
while 0 < num:
    print(num)
    num -=1
print()
# 문제3
# 3*num/2 = 63
num = 1
cal = 3*num/2
while True:
    if cal == 63:
        break
    num +=1
print(num)