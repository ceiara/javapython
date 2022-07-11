from tkinter.messagebox import showinfo
from friend import Friend

# 문제 1
f = Friend('윤성우','010-111-222')
f.get_name()
print(f.get_name())

f.get_phone()
print(f.get_phone())

#f.set_phone('010-333-444')
f.show_info()