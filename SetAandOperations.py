def set1():
    # s1 = {1,3,6,2,3,3,6,5,6,5,6,5,6,5,67,8}
    s1 = set((1,3,6,2,3,3,6,5,6,5,6,5,6,5,67,8))

    print("set is {}".format(s1), type(s1))

# set1()

def set2():
    # s1 = {1,3,6,2,3,3,6,5,6,5,6,5,6,5,67,8}
    s1 = set((1,3,6,2,3,3,6,5,6,5,6,5,67,8))
    print("set is {}".format(s1), type(s1))
    s1.add(77)
    print("set after add func is {}".format(s1), type(s1))
    s1.pop()
    print("set after pop is {}".format(s1), type(s1))
    s1.remove(3)
    print("set after remove is {}".format(s1), type(s1))

# set2()


def set3():
    s1 = { 1,2,3,4,5,7,8}
    s2=  { 4 ,5 ,6,7,8,9,10,11}
    print("set1 is {}".format(s1))
    print("set2 is {}".format(s2))
    print(" ")
    setUnion = s1.union(s2)
    print("Union of set is {}".format(setUnion))
    setInters = s1.intersection(s2)
    print("Intersection of set is {}".format(setInters))
    setSub1 = s1-s2
    print("subtraction of s1- s2 is {}".format(setSub1))
    setSub2 = s2 - s1
    print("subtraction of s2- s1 is {}".format(setSub2))


# set3()

def frozenExample():
    # immutable
    s1 = frozenset([1, 3, 5, 6, 7, 2, 3, 4, 5, 3, 4, 5, 2, 1])
    print(type(s1))
    print(s1)

frozenExample()
