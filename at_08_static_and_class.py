class MathOperations:
    factor = 2  # Class-level variable

    def __init__(self, x):
        self.x = x

    # Instance method to square the instance's x value
    def square(self):
        return self.x ** 2

    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class method to multiply a number by a class-level factor

    @classmethod
    def multiply(cls, num):
        return num * cls.factor

# Creating an instance of MathOperations
math_op = MathOperations(4)

# Using instance method
result1 = math_op.square()
print("Square of x:", result1)  # Output: 16

# Using static method
result2 = MathOperations.add(3, 5)
print("Result of addition:", result2)  # Output: 8

# Using class method
result3 = MathOperations.multiply(4)
print("Result of multiplication:", result3)  # Output: 8
