def function1():
    print("Inside Function 1")

def function2(func):
    print("Inside Function 2 ")
    func()
    print(type(func))

# aliasFunc = function1    #it creates the alias of function1
# function2(aliasFunc)

def  add(num1, num2):
    print(num1+num2)

def  sub(num1, num2):
    print(num1-num2)

def  mul(num1, num2):
    print(num1*num2)

def  div(num1, num2):
    print(num1/num2)


def execute(func):
    func(10, 20)
    func(20,30)

# execute(add)
# execute(sub)
# execute(mul)
# execute(div)

def execute1(*functions):
    for func in functions:
        func(10,20)


execute1(add,sub,mul,div)