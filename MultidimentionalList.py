def listMatrix2_2():
#    matrix = [  [11,22] ,
#                [33,44] ]

    matrix =[ ["shruti","Nishi"],
               ["Neeti","Kalyani"] ]
    print(matrix)
    print(" ")
    print(matrix[0])
    print(matrix[1])

    print(" ")

    print(matrix[0][0], matrix[0][1],matrix[1][0], matrix[1][1])

    print(" ")

    for rows in matrix:
        print(rows)

    print(" ")

    for rows in matrix:
        print(rows[0] , rows[1])

    print(" ")

    for rows in matrix:
        for values in rows:
            print(values , end=" ")


listMatrix2_2()