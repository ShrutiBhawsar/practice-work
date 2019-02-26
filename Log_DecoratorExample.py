

def log(func):
    def inner(*args , **kwargs):
        print(" inside log")
        print(" function is {}".format(func) )
        print(args , kwargs)
        func(*args, **kwargs)
        print("........................................................")
    return inner

@log
def add(p1,p2):
    print("addition is {}".format(p1+p2))

@log
def mul(p1,p2):
    print("multiplication is {}".format(p1*p2))


@log
def square(p1):
    print(" square is {}".format(p1* p1))


add(10,20)
mul(20,p2=3)
square(22)




