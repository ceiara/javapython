class Person:
    def up_age(self): # self에 p1이라는 자기 자신이 들어가게 됨.
        self.age += 1 # self.age = self.age + 1 
    def get_age(self):
        return self.age # self <- p1.age