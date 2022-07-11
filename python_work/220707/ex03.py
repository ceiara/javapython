def doA():
    lcm = 1
    while True:
        if lcm%6==0 and lcm%45==0:
            break
        lcm +=1
    print("lcm",lcm)

print()
def doB():
    num = 42
    while num>0:
        if 42%num==0 and 120%num==0:
            print(num,end=" ")
        num -=1
doB()