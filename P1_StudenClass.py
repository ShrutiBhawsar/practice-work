

class student:
    def __init__(self):
        setattr(self, 'rollno', " ")
        setattr(self, 'name', " ")
        setattr(self, 'course', " ")
        setattr(self, 'markslist', " ")

    def acceptStudent(self):
        rollno =    input("Roll no    :    ")
        name =      input("Name       :    ")
        course =    input("Course     :    ")
        marks = input("5 subjects marks :  ")
        setattr(self, 'rollno', rollno)
        setattr(self, 'name', name)
        setattr(self, 'course', course)
        markslist = list(marks.split(" "))
        setattr(self, 'markslist', markslist)

    def getInfo(self):
        print("Roll No = {} ,".format(getattr(self, 'rollno')), end= " ")
        print("Name    = {} ,".format(getattr(self, 'name')),end= " ")
        print("Course  = {} ,".format(getattr(self, 'course')),end=" ")
        print("Marks   = {} ,".format(getattr(self, 'markslist')),end= " ")

    def ifFail(self):
        fail  = False
        for mark in getattr(self, 'markslist'):
            if mark <= '45':
                fail = True
                print("Student failed in the exam")
                break;

        if fail == False:
            print("Student passed in the exam ")
        print()

def main_function():
    studentList= []
    print(" Enter 5 students info :")
    print("  student 1 info :")
    s1= student()
    s1.acceptStudent()
    studentList.append(s1.__dict__)

    print("  student 2 info :")
    s2= student()
    s2.acceptStudent()
    studentList.append(s2.__dict__)
    #
    # print("  student 3 info :")
    # s3 = student()
    # s3.acceptStudent()
    # studentList.append(s3)
    #
    # print("  student 4 info :")
    # s4=student()
    # s4.acceptStudent()
    # studentList.append(s4)
    #
    # print("  student 5 info :")
    # s5 = student()
    # s5.acceptStudent()
    # studentList.append(s5)

    print(".............. The Students info are .....................: ")
    s1.getInfo()
    s1.ifFail()

    s2.getInfo()
    s2.ifFail()
    #
    # s3.getInfo()
    # s3.ifFail()
    #
    # s4.getInfo()
    # s4.ifFail()
    #
    # s5.getInfo()
    # s5.ifFail()

    Input_roll = input( " Enter the roll number to display stutent info : ")
    for st in studentList:
        print(type(st))
        if st['rollno'] == Input_roll:
             print(st)
             break;

    # print(studentList)


main_function()

