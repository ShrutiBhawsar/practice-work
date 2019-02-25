numbers = [1,2,3,4,5,6,7,8,9,10]

def EvenFunction1():
    evenList = []
    for number in numbers:
        if number % 2 == 0:
            evenList.append(number)
    print(numbers)
    print("Even Number List is {}".format(evenList))

# EvenFunction1()

def OddFunction1():
    oddList = []
    for number in numbers:
        if number != 0:
            oddList.append(number)
    print(numbers)
    print("Odd Number List is {}".format(oddList))

# OddFunction1()

def EvenFunction2():
    evenList = list(filter(lambda number : number % 2 == 0,numbers))
    print(numbers)
    print("Even Number List using filter method is  {}".format(evenList))

# EvenFunction2()

def OddFunction2():
    oddList = list(filter(lambda number : number %2 != 0, numbers))
    print(numbers)
    print("Odd Number List using filter method is {}".format(oddList))

# OddFunction2()

def SquareOfEven():
    evenList = list(filter(lambda number : number % 2 == 0,numbers))
    print("Even Number List using filter method is  {}".format(evenList))
    squareOfEven = list(map(lambda n: n* n , evenList))
    print("Square of Even Number List using map method is  {}".format(squareOfEven))

# SquareOfEven()

def SquareOfOdd():
    oddList = list(filter(lambda number : number % 2 != 0,numbers))
    print("Odd Number List using filter method is  {}".format(oddList))
    squareOfOdd = list(map(lambda n: n* n , oddList))
    print("Square of Odd Number List using map method is  {}".format(squareOfOdd))

SquareOfOdd()
