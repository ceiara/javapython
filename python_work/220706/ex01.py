from soupsieve import select
from car import Car

def result():
    c1 = Car()
    print('result')
    while True:
        print('속도입력')
        print('속도출력')
        select = int(input())
        if select ==1:
            speed = input('속도를 입력하세요')
            c1.speed = speed
        else:
            print("속도 = ",c1.speed)
result()
