class AA:
    number = 0
    #생성자
    def __init__(self, number):
        print(self.number)
        self.number = number
        print(self.number)
        print("construct exit")
    def print(self):
        print('number = ',self.number)
        if(self.number>0):
            print("양수입니다")
        else:
            print("음수입니다.")
    def inputnumber(self):
        self.number = eval(input("숫자를 입력하세요"))