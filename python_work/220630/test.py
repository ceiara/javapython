# 문제 1
def int_div(a,b):
    c = a//b
    d = a%b
    print('몫: ',c)
    print('나머지: ',d)

int_div(5,2)

# 문제 2
def bet_sum(n,h):
    sum = 0
    for i in range(n+1,h):
        sum += i
    print(sum)

bet_sum(2,5)
bet_sum(1,5)
