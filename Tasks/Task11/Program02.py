
def CountDigit(No):
    Count = 0
    
    while(No > 0):
        No //= 10
        Count += 1
        
    return Count

def main():
    Value = int(input("Enter number : "))
    
    Ret = CountDigit(Value)
    
    print("Total digits in number are: ", Ret)

if __name__ == "__main__":
    main()