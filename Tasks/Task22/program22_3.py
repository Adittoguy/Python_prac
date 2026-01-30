class Arithmetic:
    # constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # instance method to accept values
    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    # instance method for addition
    def Addition(self):
        return self.Value1 + self.Value2

    # instance method for subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # instance method for multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # instance method for division
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        return self.Value1 / self.Value2


# creating multiple objects
Obj1 = Arithmetic()
Obj2 = Arithmetic()

# first object operations
Obj1.Accept()
print("Addition:", Obj1.Addition())
print("Subtraction:", Obj1.Subtraction())
print("Multiplication:", Obj1.Multiplication())
print("Division:", Obj1.Division())
print("--------------------------")

# second object operations
Obj2.Accept()
print("Addition:", Obj2.Addition())
print("Subtraction:", Obj2.Subtraction())
print("Multiplication:", Obj2.Multiplication())
print("Division:", Obj2.Division())
