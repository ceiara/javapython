def doA():
    num = 0
    while num < 10:
        print("num = ",num)
        num +=1

def doB():
    num = 9
    while num > -1:
        print("num = ",num)
        num -= 1
doA()
doB()

print()

num = 1
while 3*num/2 != 63:
    num +=1

print("num = ",num)

num = 1
while True:
    if 3*num/2 == 63:
        break
    num +=1
print("num = ",num)
