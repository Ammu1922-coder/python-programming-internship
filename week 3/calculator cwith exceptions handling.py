class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b

        except ZeroDivisionError:
            return "Cannot divide by zero!"


calc = Calculator()

try:

    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    print("Addition:", calc.add(a, b))
    print("Subtraction:", calc.sub(a, b))
    print("Multiplication:", calc.mul(a, b))
    print("Division:", calc.div(a, b))

except ValueError:
    print("Please enter valid numbers.")