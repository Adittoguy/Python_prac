def Factors(No):
    sum = 0
    
    for i in range(1, No):
        if(No % i == 0):
            sum += i
    
    return sum

def main():
    Value = int(input("Enter Number: "))
    
    ret = Factors(Value)
    
    print("Sum of Factors are: ", ret)
    
if __name__ == "__main__":
    main()