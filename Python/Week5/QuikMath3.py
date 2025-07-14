#1. Create a class called calculator

#2. Create a function in the class for each mathematical operation: Addition, Multiplication, Division, Subtraction

#3. Outside of your class definition, create an instance of your calculator class

#4. Call each function in your calculator class and store each output into a variable. Use any values for arguments.

#5. Print all your variables to the console
class Calculator:
    def Add(self, x, y):
        return x + y
    def Sub(self, x, y):
        return x - y
    def Mul(self, x, y):
        return x * y
    def Div(self, x, y):
        return x / y

calculator = Calculator()
Sum = calculator.Add(4, 5)
Difference = calculator.Sub(10, 4)
Product = calculator.Mul(6, 7)
Dividend = calculator.Div(20, 5)
print(Sum)
print(Difference)
print(Product)
print(Dividend)