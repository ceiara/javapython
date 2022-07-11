from car1 import Car

def main():
    c1 = Car()
    while True:
        print("1. 속도입력")
        print("2. 속도출력")
        select = int(input())
        if select == 1:
            speed = input('속도를 입력하세요')
            c1.speed = speed
        else:
            print("현재속도는",c1.speed)
main()