#using lambda peforming the arithemetic operations on  2 numbers


def execute1(func, string):
    print(".....{}.......".format(string))
    print("result is {}".format(func(30,10)))
    print("result is {}".format(func(30,10)))
    print("result is {}".format(func(30,10)))

execute1(lambda x,y : x + y,"Addition")
execute1(lambda x,y : x-y ,"Subtraction")
execute1(lambda x,y : x*y, "Multiplication")
execute1(lambda x,y : x/y , "Division")



