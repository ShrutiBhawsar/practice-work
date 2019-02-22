
def function1(p1,p2) :
    """
    it does the addition
    :param p1: receives int/float value
    :param p2: receives int/float value
    :return: return the sum of 2 addition
    """
    result = p1 + p2
    return(result)

    #  addition = function1(10,20)
    # print(" Addition  is  {}".format(addition))

def function2(p1,p2):
    """
    :param p1: receives int/float value
    :param p2: receives int/float value
    :return: it does not return any value
    """
    result = p1 + p2
    #print(" Result is  {}".format(result))


# function2(12, 13)
# addition = function2(11,11)
# print("addition is {}".format(addition))     # it return None as nothing is returning in the function definition

# Returning values in tuple
def function3(p1,p2):
    add = p1+p2
    sub = p1-p2
    dev = p1/p2
    mul = p1*p2
    return (add,sub,dev,mul)  # returning values in tuple

# result = function3(12,24)
# ...........1st way of printing..................
# print("addition is {} ".format(result[0]))
# print("substraction is {} ".format(result[1]))
# print("devision is {} ".format(result[2]))
# print("multiplication  is {} ".format(result[3]))

# ...........1st way of printing..................

# print("result is {}".format(result), type(result))          # it returns the tuple

# ...........1st way of printing..................

# for value in result:
#     print("value")



