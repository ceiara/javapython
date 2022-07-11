from cgi import print_arguments


ds = (1,2,3)
def to_list():
    a = list(ds)
    print(a)
to_list()

ds ="hello"
def to_list():
    a = list(ds)
    print(a)
to_list()

ds ="hello"
def to_list():
    list(ds)
    print(ds)
to_list()