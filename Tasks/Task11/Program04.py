def Reverse(No):
    RevNum = 0
    
    while (No != 0):
        Digit = No % 10
        RevNum = RevNum * 10 + Digit
        No //= 10
        
    return RevNum

def main():
    Value = int(input("Enter number: "))
    
    Ret = Reverse(Value)
    
    print("Reversed number is : ", Ret)

if __name__ == "__main__":
    main()