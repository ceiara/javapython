def main():
    num = int(input("숫자를 입력하세요"))
    if num<0:
        print(num,"은 0보다 작습니다")
    elif 10 > num >= 0:
        print(num,"은 0이상 10미만입니다")
    elif 20 > num >= 10:
        print(num,"은 10이상 20미만입니다")
    else:
        print(num,"은 20이상입니다.")

main()