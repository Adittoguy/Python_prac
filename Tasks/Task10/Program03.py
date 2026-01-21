def Factorial(No):
    
    Fact = 1
    
    for i in range(1, No + 1):
        Fact *= i    
    
    return Fact

def main():
    Value = int(input("Enter number: "))
    
    Ret = Factorial(Value)
    
    print("Factorial of given number: ", Ret)
    
if __name__ == "__main__":
    main()