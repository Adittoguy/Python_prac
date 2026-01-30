class Numbers:
    # constructor
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    # check prime number
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    # display all factors
    def Factors(self):
        print("Factors are:", end=" ")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # return sum of factors
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        return sum

    # check perfect number
    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


# creating multiple objects
Obj1 = Numbers()
Obj2 = Numbers()

# calling methods for first object
print("Is Prime:", Obj1.ChkPrime())
Obj1.Factors()
print("Sum of Factors:", Obj1.SumFactors())
print("Is Perfect:", Obj1.ChkPerfect())
print("---------------------------")

# calling methods for second object
print("Is Prime:", Obj2.ChkPrime())
Obj2.Factors()
print("Sum of Factors:", Obj2.SumFactors())
print("Is Perfect:", Obj2.ChkPerfect())
