class Student():
    # class variable
    # the number of students
    # all changes amde by other objects and instances,
    # can be seen
    pop = 0

    def __init__(self, name, avg):
        self.name = name
        self.avg = avg
        print('Hi, how are you? My name is', self.name)
        # remember to b=put the class that defines the cls var
        Student.pop += 1

        #when this is created, the student adds to the population

    def leave(self):
        Student.pop -= 1

        if Student.pop == 0:
            print('No students available')
        else:
            print(Student.pop, ':students left')

    def grades(self):
        print('My avg is', self.avg)

    @classmethod

    def how_many(cls):
        print('Total Students:', cls.pop)

stu_1 = Student('Bob', '72')
stu_1.grades()
Student.how_many()
stu_1.leave()
Student.how_many()
