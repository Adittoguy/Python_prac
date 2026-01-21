
def CountDigit(No):
    sum = 0
    
    while(No > 0):
        Digit = No % 10
        sum += Digit
        No //= 10
               
    return sum

def main():
    Value = int(input("Enter number : "))
    
    Ret = CountDigit(Value)
    
    print("Total digits in number are: ", Ret)

if __name__ == "__main__":
    main()