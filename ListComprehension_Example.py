numbers = list(range(1,11))

def Square():
    squareList = [n * n for n in numbers]
    print(numbers)
    print(squareList)

# Square()

def Even():
    evenList = [ n for n in numbers if n % 2 == 0]
    print(numbers)
    print("Even number list is {} ".format(evenList))

# Even()

def squares_of_even():
    squareOfEvenList = [ n* n for n in numbers if n %2 == 0]
    print(numbers)
    print("Square of even numbers list is {}".format(squareOfEvenList))

# squares_of_even()


def cars():
    max = 5
    cars = [
        {'model': 'i20', 'company': 'hyudai', 'price': 7.5},
        {'model': 'i10', 'company': 'hyudai', 'price': 5.0},
        {'model': 'fabia', 'company': 'skoda', 'price': 4.5},
        {'model': 'nano', 'company': 'tata', 'price': 1.5}
    ]

    result1 = [ car for car in cars if car['price'] < max]
    print(result1)

    result2 = [ car["model"]  for car in cars if car["price"] < max]
    print(result2)

    #tuple
    result3 = [ (car["model"], car["price"])  for car in cars if car["price"] < max]
    print(result3)

    #dictonary
    result4 = [{"model": car["model"]} for car in cars if car["price"] < max]
    print(result4)


cars()
