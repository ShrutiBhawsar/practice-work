numbers = [1,2,3,4,5,6,7,8,9,10]

def Square(n):
    """
    :param n: integer
    :return: square of a given number
    """
    return (n*n)

def function1():
    """
    it is calculating the square of each value in the list
    :return:
    """
    for number in numbers:
        sqr =Square(number)
        print("square : {} ".format(sqr))

# function1()

def function2():
    """
    it is calculating a square for each value and putting it into a list
    :return:
    """
    squareList = []     #declaring an epmty list
    for number in numbers:
        squareList.append(Square(number))    # it is adding the sqaure of each value in the list
    print(numbers)
    print(squareList)

# function2()


def  function3():
    """
        # map is calling function Square for each value in th numbers List nd appending it to the squareList
   :return:
    """
    squareList = list(map(Square,numbers))
    print(numbers)
    print(squareList)

# function3()


def function4():
    """
    Using lambda , square of each value in numbers is calculated
    :return:
    """
    squareList = list(map(lambda n: n*n , numbers))
    print(numbers)
    print(squareList)

function4()



