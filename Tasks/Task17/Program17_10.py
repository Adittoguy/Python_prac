def Digit(No):
    sum = 0
    digit = 0
    
    while(No > 0):
        digit = No % 10
        sum += digit
        No //= 10
        
    return sum
        

def main():
    Value = int(input("Enter number: "))
    
    ret = Digit(Value)
    
    print("Sum of Digits in number are: ", ret)
    
if __name__ == "__main__":
    main()