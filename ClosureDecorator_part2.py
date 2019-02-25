def execute(func, p1, p2):
    print("................................")
    func(p1,p2)
    print("................................")


def add1(p1,p2):
    print( p1+p2)

def mul(p1,p2):
    print(p1*p2)

def div(p1,p2):
    print(p1/p2)


# execute(add,10,20)
# execute(mul, 20,3)

# decorator without parameters
def decorate(func):
    def inner():
        print("...............................")
        func()
        print("...............................")

    return inner

@decorate
def add1():
    p1= 10
    p2 = 30
    print("addition is {}".format( p1+p2))

@decorate
def mul1():
    p1 = 10
    p2 = 30
    print("multiplication is {}".format(p1*p2))

@decorate
def div1():
    p1 = 10
    p2 = 2
    print("division is {}".format(p1/p2))

# addressOfFunc = decorate(add1)
# addressOfFunc()
#..............
# add1()
# mul1()
# div1()



