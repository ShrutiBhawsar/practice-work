def functionA():
    print("In function 1")
    number = [1,2,3,4,5]
    print("Numbers are  - {} and Type is {} ".format(number ,type(number)))

# functionA()

def functionA():
    print("In function 1")
    numbers = [1,2,3,4,5]
    for value in numbers :
        print("Values are  - {} and Type is {} ".format(value ,type(value)))

# functionA()

def functionT():
    List1 =[ 1, 'abc' , True, 1.45]
    print("List Values  are  - {} and Type is {} ".format(List1 ,type(List1)))


#Range function - it exclude the last value
#length function
def functionB():
    print("In function B")
    numbers = list(range(0,11))
    Length= len(numbers)
    print("Values are  - {} and Type is {} ".format(numbers ,type(numbers)))
    print("Length of list is   - {} and Type is {} ".format(Length ,type(Length)))

# functionB()

# Performing different operation on List
def functionC():
    print("In function C")
    numbers = [1,2,3,4,5]
    print("Values are  - {} and Type is {} ".format(numbers ,type(numbers)))
    numbers.append(11)                                       #append adds element at the last
    print("After Appending , List is :  {}  ".format(numbers))
    numbers.insert(2, 22)                                   # insert adds element at the given index
    print("After inserting , List is :  {}  ".format(numbers))
    numbers.remove(3)                                        #remove used to delete any element
    print("After removing , List is :  {}  ".format(numbers))
    numbers.pop()                                           # pops remove the last element
    print("After popping , List is :  {}  ".format(numbers))
    numbers.reverse()
    print("After  reversing , List is :  {}  ".format(numbers))
    numbers.sort()  # sort in ascending order
    print("After  sorting , List is :  {}  ".format(numbers))
    numbers.sort(reverse= True)                                          # sort in ascending order
    print("After  sorting in descending order , List is :  {}  ".format(numbers))
    
functionC()

