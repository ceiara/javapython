from pickletools import pystring

#quiz2
st = [1,2,3]
print(st)
st.pop(-1)
print(st)

#quiz 3
print()
st = [1,2,3,4]
st[:] = []
print(st)

# quiz 4
print()
st = []
for i in range(0,10):
    i+=1
    st.append(i)
    st.remove(i)
print(st)

# quiz 5
print()
st = []
for i in range(10):
    i+=1
    st.append(i)
print(st)


# quiz 6
print()
st = [1,2]
st[2:] = [3,4,5]
print(st)