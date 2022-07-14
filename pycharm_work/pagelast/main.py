from a import Friend

mylist = [Friend("윤지민", "010-111-222"), Friend("이선준", "010-333-444"), Friend("장지우", "010-555-5555"), Friend("윤지윤", "010-777-888")]

for f in mylist:
    if f.get_name() == '장지우':
        f.set_phone("010-999-999")
    #if f.get_name().startswith('윤'):
     #   print(f)
for f in mylist:
    print(f)