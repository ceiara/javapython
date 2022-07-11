# 문제 1
import gc

def main():
    lcm = 45
    i = 1
    while 0<i:
        lcm+=i
        i +=1
        if (lcm%6 == 0) and (lcm%45 == 0):
            print(lcm)
            break   
main()
print()
# 문제 2
def main():
    gcm = 42
    while 0<gcm:
        gcm -=1
        if (42%gcm == 0) and (120%gcm == 0):
            print(gcm)
            break
main()