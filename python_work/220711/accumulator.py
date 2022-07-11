# sum = 0

class Accumulator:
    def __init__(self):
        self.sum = 0
    # @staticmethod
    def add(self,i):
        # global sum #global: 밖에 선언된 전역변수를 사용하겠다
        self.sum += i
    # @staticmethod
    def showResult(self):
        print(f"sum = {self.sum}") #python 3.ver에서만 사용가능