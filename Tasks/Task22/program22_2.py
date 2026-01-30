class Circle:
    # class variable
    PI = 3.14

    # constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # instance method to accept radius
    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    # instance method to calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # instance method to calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # instance method to display values
    def Display(self):
        print("Radius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)
        print("-------------------------")


# creating multiple objects
Obj1 = Circle()
Obj2 = Circle()

# invoking methods for first object
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

# invoking methods for second object
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()
