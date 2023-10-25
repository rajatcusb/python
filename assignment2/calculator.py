class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

    def subtract(self, num):
        self.value -= num

    def multiply(self, num):
        self.value *= num

    def divide(self, num):
        if num != 0:
            self.value /= num
        else:
            print("Cannot divide by zero.")

    # Operator overloading methods
    def __add__(self, num):
        return self.value + num

    def __sub__(self, num):
        return self.value - num

    def __mul__(self, num):
        return self.value * num

    def __truediv__(self, num):
        if num != 0:
            return self.value / num
        else:
            return "Cannot divide by zero."

# Create a Calculator object
calculator = Calculator(10)

# Using methods for basic arithmetic operations
calculator.add(5)
calculator.subtract(3)
calculator.multiply(4)
calculator.divide(2)

print("Value after basic operations:", calculator.value)

# Using operator overloading
result1 = calculator + 5
result2 = calculator - 2
result3 = calculator * 3
result4 = calculator / 2

print("Results using operator overloading:")
print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)
