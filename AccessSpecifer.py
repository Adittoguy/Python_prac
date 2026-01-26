class Demo:
    
    def __init__(self):
        self.No1 = 10       # public
        self._No2 = 20      # (_)   protected
        self.__No3 = 30     # (__)  private

obj = Demo()
print(obj.No1)
print(obj.No2)
print(obj.No3)
