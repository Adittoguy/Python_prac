class Demo:
    
    No = 10
    
    def __init__(self, A, B):
        self.Value1 = A
        self.Value2 = B
        
    def fun(self):                  # Instance Method
        print("Inside Instance Method fun: ", self.Value1, self.Value2)
    
    @classmethod                    # Decorator
    def sun(cls):                   # Class Method
        print("Inside Class Method sun: ", cls.No)
        
    @staticmethod                   # Decorator : IMP for interpretor
    def gun():                      # Static Method
        print("Inside Static Method gun : ", Demo.No)
        

Demo.sun()

print("Class Variable : ", Demo.No)        

obj = Demo(11, 21)
obj.fun()

print("Instance Variable : ", obj.Value1, obj.Value2)

Demo.gun()