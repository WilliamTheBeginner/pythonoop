class Member():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('New Member: {}'.format(self.name))

    def details(self):
        '''Member Deatils'''
        print('Name: {} \n Age: {}'.format(self.name, self.age))

class Teacher(Member):
    def __init__(self, name, age, salary):
        Member.__init__(self, name, age)
        self.salary = salary
        print('New Teacher: {}'.format(self.name))

    def details(self):
        Member.details(self)
        print('Salary: {}'.format(self.salary))

class Student(Member):
    def __init__(self, name, age, marks):
        Member.__init__(self, name, age)
        self.marks = marks
        print('New Student: {} {}'.format(self.name, age))

    def details(self):
        Member.details(self)
        print('Marks: {}'.format(self.marks))

t1 = Teacher('Mrs. Bob', 20, 50000)
s1 = Student('Joe', 10, 98)

members = [t1, s1]

for member in members:
    # Both Teachers and Students
    member.details()
