#allows you to do any initialization
# e.g. passing initial values to the object

class Student():
    def __init__(self, name):
        self.name = name

    def greetings(self):
        print('Hello, how are you?', 'My name is', self.name)

s1 = Student('Bob')
s1.greetings()

class Employee():
    #instance attributes
    def __init__(self, name):
        self.name = name

    def greetings_withname(self):
        print('Hello, my name is', self.name)

# the init method is not called
emp_1 = Employee('Bob')
emp_1.greetings_withname()
