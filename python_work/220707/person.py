class Person:
    name=""
    def __init__(self,name): #self 생략불가, name에 java가 들어감
        self.name = name

    def __str__(self):
        return "Person "+self.name 