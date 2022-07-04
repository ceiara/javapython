# 문제 1. "안녕하세요."를 총 5회 출력하는 코드를 for와 range 기반으로 작성해보자.
for i in range(0,5):
    print("안녕하세요.")

# 문제 2. 구구단 7단 전부를 출력하는 코드를 for와 range 기반으로 작성해보자
for i in range(1,10):
    print("7 *",i)
    sum = 7
    sum *= i
    print(sum)

# 문제 3. 다음 수식의 결과를 계산해서 그 값을 반환하는 함수를 for와 range 기반으로 정의해보자.
# x의 y승
# 예를 들어서 함수의 이름이 exp라 할 때, exp(2,3)의 형태로 호출되면 2의 3승 = 2*2*2 = 8이므로 8이 반환되어야 한다. 이 문제는 함수 안에 for 루프를 넣어서 작성해야 하므로 조금 어렵게 느낄 수 있다.

#def exp():
#    for i in 

# 문제 4. "반갑습니다"를 여러 번 출력하는 greet이라는 이름의 함수를 만들어보자. 단, 몇 번 출력할지는 프로그램 사용자에게 묻고 입력받는 형태로 작성하자
def greet():
    a = input("인사를 몇 번 할까요?")
    print(a)
    b = eval(a)
    for i in range(b):
        print("반갑습니다.")

greet()