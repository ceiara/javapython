class Friend:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def show_info(self):
        return f"이름: {self.name}\n전화번호: {self.phone}"