class Parent:
    def __init__(self):
        print("Inside Parent constructor")
        self.No1 = 10
        self.No2 = 20
        
    def fun(self):
        print("Inside fun method of parent", self.No1, self.No2)
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor")
        self.A = 11
        self.B = 21
        
    def sun(self):
        print("Inside sun method of child", self.No1, self.No2, self.A, self.B)
        
cobj = Child()

cobj.fun()
cobj.sun()

print(cobj.No1)
print(cobj.No2)

print(cobj.A)
print(cobj.B)

