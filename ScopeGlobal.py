number = 100

print("Not in any function , value of global variable is  {}".format(number))

def function1():
    number = 232
    print("Inside a  function , value of global variable is now  {}".format(number))      #number = 232


# function1()

def function2():
    print("Inside  function 2 , value of global variable is now  {}".format(number))     #number = 100

# function2()

# print("Not in any function , value of global variable is   {}".format(number))

def function3():
    global number
    number = 3433
    print("Inside function 3 global keyword , value of global variable is now  {}".format(number))      #number = 232


function3()

def function4():
    # print("Inside  function 4 , value of global variable is now  {}".format(number))     #number = 100
    number = 454
    print("Inside  function 4 , value of global variable is now  {}".format(number))     #number = 100

function4()

print("Not in any function , value of global variable is   {}".format(number))


