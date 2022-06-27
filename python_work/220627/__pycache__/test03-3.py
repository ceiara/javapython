# 문제 1. 1, 3, 5, 9의 합을 계산해서 그 결과를 출력하는 코드를 for 루프를 기반으로 작성해보자
sum = 0
for i in[1,3,5,9]:
    sum += i
print(sum)

# 문제 2. 1부터 10까지의 곱의 결과를 계산해서 그 결과를 출력하는 코드를 for 루프를 기반으로 작성해보자.
sum = 1
for i in range(1,11):
    sum *= i
print(sum)

# 문제 3. 구구단에서 7단 전부를 출력하는 코드를 for 루프를 기반으로 작성해보자

for i in range(1,10):
    print("7 *",i )
    sum = 7
    sum *= i
    print(sum)

# 문제 4. 구구단 7단을 전부 출력하되 거꾸로(7*9 = 63부터) 출력하는 코드를 for 루프를 기반으로 작성해보자.
for i in [9,8,7,6,5,4,3,2,1]:
    print("7 *",i )
    a = 7
    a *= i
    print(a)