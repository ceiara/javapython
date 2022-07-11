from numpy import number


class Friend:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.number
    def set_phone(self):
        print(self.number)
    def show_info(self):
        print(f"이름: {self.name}, 전화번호: {self.number}")