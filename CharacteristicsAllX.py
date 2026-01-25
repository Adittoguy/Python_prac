class Demo:
    
    No = 10
    
    def __init__(self, A, B):
        self.Value1 = A
        self.Value2 = B
        
print("Class Variable: ", Demo.No)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

# print(obj1.No)                Allowed

print("Instance Vaiable of obj1 : ",obj1.Value1, obj1.Value2)
print("Instance Vaiable of obj2 : ",obj2.Value1, obj2.Value2)

obj1.Value1 = 15

Demo.No = 0

print("Instance Vaiable of obj1 : ",obj1.Value1, obj1.Value2)
print("Instance Vaiable of obj2 : ",obj2.Value1, obj2.Value2)

print(obj1.No)
print(obj2.No)
