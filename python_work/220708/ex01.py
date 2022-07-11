# p.162 문제 1
for i in range(1,10):
    if (7 * i)%2 == 0:
        print(7 * i,end=' ')
print()

#문제 2
num = 2
while(num<100):
    if num%2!=0 and num%3!=0:
        print(num,end=' ')
    num +=1

print()
# 문제 3
num = 2
while(num<100):
    num +=1
    if num%2!=0 or num%3!=0:
        continue
    print(num,end=' ')
    
print()
#p.165
for dan in range(2,10):
    for i in range(1,10):
        print(dan*i,end=' ')
    print()