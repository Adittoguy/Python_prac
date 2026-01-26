def Factorial(No):
    fact = 1
    
    for i in range(1, No + 1):
        fact *= i

    return fact

def main():
    Value = int(input("Enter Number: "))
    
    ret = Factorial(Value)
    
    print("Factorial is : ",ret)
    
if __name__ == "__main__":
    main()