#performing different operation using lambda

cars = [
        ('i20'   , 'hyundai', 7.5 ),        # Yes
        ('innova', 'toyota' , 25.5),     # No
        ('nano'  , 'tata'   , 2.5 )           # Yes
    ]

def CarDefination1():
    max= 10
    CarsPrice = list(map(lambda car : 'price of {} is  {}'.format(car[0],car[2]) ,cars ))
    print(CarsPrice)

# CarDefination1()

def CarDefination2():
    """
    it returns True if the car is affordable and false if it is not affordable
    :return:
    """
    max= 10
    isAffordablecar = list(map(lambda car : car[2]<= 10 , cars))
    print(isAffordablecar)

# CarDefination2()

def CarDefination3():
    """
    It will print the list of car that is affordable
    Filter returns boolean values. For "True ", it will  put the corresponding object/value in the list.
    it excludes the objects whose return value is "False" after processing
    :return:
    """
    max=10
    affordableCar= list(filter(lambda car : car[2]<= 10 , cars))
    print("The list of car details that are affordabl {}".format(affordableCar))

# CarDefination3()


