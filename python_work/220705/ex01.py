st = 'The Espresso Sprit'
print(st.upper())

cnt = 0
for i in st:
    if i=='E':
        print(i)
        print(cnt)
    cnt+=1
print(st.find('E'))

myst = "한글입니다.\n 좋네요"
print(myst)

myst = "한글입니다.\t 좋네요"
print(myst)
myst = "한글입니다.\"좋네요"
print(myst)
myst = "한글입니다.'좋네요"
print(myst)

mylist = [1,2,3,4,5]
del mylist[3:]
print(mylist)

mylist = [1,2,3,4,5]
del mylist #변수자체를 지운것 mylist[:] - 전체 내용을 지운것
print(mylist)