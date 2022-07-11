st = [1,2,3,4,5]
a =[]
def add1(s):
    for s in st:
        s +=1
        a.append(s)
    return a
print(add1(a))