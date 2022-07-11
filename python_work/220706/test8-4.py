i = 1 
num = 2 
for num in range(2,10,+1):
    for i in range(1,10,+1):
        num *=i
        print(num,end=' ')
