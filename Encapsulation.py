class Arithematic:
    
    def __init__(self, A, B):       # Magic Method
        self.No1 = A
        self.No2 = B
        print("Object gets created successfully")
        
    def Addition(self):             # Instance Method
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):         # Instance Method
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

obj1 = Arithematic(11, 10)          # Arithematic(id(self, 11, 10)) -> __init__(id(slef, 11, 10))
obj2 = Arithematic(21, 20)          

Ret = obj1.Addition()               # Addition(id(obj1)) -> Addition(1000)
print("Addition is : ", Ret)

Ret = obj2.Substraction()           # Substraction(id(obj1)) -> Substraction(1000)
print("Substraction is : ", Ret)

