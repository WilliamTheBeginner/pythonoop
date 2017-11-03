"""class Calculator():
    def add(v1, v2):
        return v1 + v2
    def subtract(v3, v4):
        return v3 - v4
    def multiply(v5, v6):
        return v5 * v6
    def divide(v7, v8):
        return v7 // v8

print(Calculator.add(1,3))

print(Calculator.subtract(9, 4))

print(Calculator.multiply(3, 6))

print(Calculator.divide(10, 5))

# if there is no self, you don't need to provide an instance for it
"""
class Employee():
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 0
        print('Initialized Employee {}'.format(self.name))

    def raise_sal(self, raiseamt):
        self.salary += raiseamt
        #return salary doesn't really raise
        print(self.salary)
        print('Raising salary of {} by {}.'.format(self.name, raiseamt))
        print('New salary is {}'.format(self.salary))
    def cut_sal(self, cutamt):
        self.salary -= cutamt
        print(self.salary)
        print('Cutting salary of {} by {}.'.format(self.name, cutamt))
        print('New Salary is {}'.format(self.salary))

e1 = Employee('Josh', 20)
e1.raise_sal(0.20)
e2 = Employee('Ravi', 10)
e2.raise_sal(0.01)
e1.cut_sal(20)
