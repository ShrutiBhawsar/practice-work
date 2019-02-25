
n= 111

def outer():
    num = 100
    global  n
    n= 333
    print(n)
    print("Inside Outer FUnction, value of num is {}".format(num))


    def inner():
        nonlocal num
        # print("Inside inner , the value of num is  {}".format(num))
        num = 232
        global n
        n= 444
        print( n)
        print("Inside inner , the value of num is  {}".format(num))

    inner()
    print(n)
    print("after inner  function , the value of num is  {}".format(num))

outer()
# print("outside outer  , the value of num is  {}".format(num))
print(n)

