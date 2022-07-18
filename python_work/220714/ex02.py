'''
page 243
'''
from friend import Friend

f = Friend('윤성우', '010-111-222')
print(f.get_name())
print(f.get_phone())
print()

f.set_phone('010-333-444')
print(f.show_info())

mylist = [Friend('윤지민','010-111-222'), Friend('이선준','010-333-444'), Friend('장지우','010-555-666'), Friend('윤지율','010-777-888')]