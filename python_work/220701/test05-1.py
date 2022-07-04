#문제1
st = [1,2,3,4]
print(st[0])
print(st[1])
print(st[2])
print(st[3])

#문제2
st = [1,2,3,4]
print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])

#문제3
st = [1,2,3,4]
st[0] = 2
st[1] = 3
st[2] = 4
st[3] = 5
print(st)

#문제4
st = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    st[i] += 1
print(st)

#문제5
def change(x,y):
    st = [1,2,3,4,5,6]
    st[0] = x
    st[-1] = y
    print(st)
change(2,7)

