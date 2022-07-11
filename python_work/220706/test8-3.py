# 문제 1
i = 0
while i <10:
    print(7 * i)
    i +=2
print()
#문제 2
i = 2
while i <100:
    i +=1
    if (i%2!=0) and (i%3!=0): 
        print(i)
print()
#문제 3
i = 2
while i <100:
    i +=1
    if (i%2!=0) and (i%3!=0):
        print(i)
    else: 
        continue
        print('its worng')
    