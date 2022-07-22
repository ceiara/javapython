def doA():
    print("doA 1111111")
    yield 1
    print("doA 22222222")
    yield 2
    print("doA 33333333")
    yield 3

a = doA()

print(type(a))
ret = next(a)
print('ret = ', ret)
ret = next(a)
print('ret = ', ret)
ret = next(a)
print('ret = ', ret)


