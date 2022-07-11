from person import Person

# 메모리 상에 올림.
p1 = Person()
p2 = Person()
p3 = Person()

p1.age = 39 # 추가
p1.up_age()
print(p1.get_age())

p2.age = 59
p2.up_age()
print(p2.get_age())

n = 100
print(type(n))

a = [1,2,3,4]
print(type(a))
a.remove(1)
print(a)

# python의 모든 값은 객체 형태이다.