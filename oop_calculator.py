class Calculator():
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
