def dectionaryA():
    person = { 'name' : 'Shruti', 'age' : 24 ,'gender' :'female'}
    print(person)
    print("")

    print(person['name'] , person['age'], person['gender'])
    print()

    for key in person:
        print(key, end=" ")
    print()

    for key in person:
        print("{} = {} , ".format( key, person[key]), end=" ")


# dectionaryA()

def ListDictionay():
    employeeInfo = [   { 'Emp-name' : 'Shruti', 'Company' : 'amazon' ,'phone' : +910383746},
                      {'Emp-name': 'Neet',  'Company': 'Hcl', 'phone': +121212},
                      {'Emp-name': 'Shweta', 'Company': 'flipcart', 'phone': +7453746},
                      {'Emp-name': 'pinky', 'Company': 'myntra', 'phone': +454545}
                    ]

    print(employeeInfo)
    print()

    for info in employeeInfo:
        print(info)

    print()

    for info in employeeInfo:
        print(info['Emp-name'] , info['Company'], info['phone'])

    print()
    for info in employeeInfo:
        for value in info:
            print("{} = {} , ".format(value, info[value]),end=" ")
        print()

ListDictionay()
