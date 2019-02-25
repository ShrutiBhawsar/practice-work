
#function inside a function
def execute1(p1,p2):
    def add(p1,p2):
        return p1+p2

    def multiply(p1,p2):
        return p1 *p2

    addition = add(p1,p2)
    multi = multiply(p1,p2)
    return (addition,multi)

# result = execute1(10,20 )
# print(result)


#closure

def ExecuteClosure(p1,p2):
    print("inside ExecuteClosure ")
    def add():
        return p1+p2

    return add

AddressOfAdd = ExecuteClosure(10,20)
result = AddressOfAdd()
print(result)

