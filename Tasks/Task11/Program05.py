def Palindrom(No):
    RevNum = 0
    temp = No
    
    while (temp != 0):
        Digit = temp % 10
        RevNum = RevNum * 10 + Digit
        temp //= 10
        
    if(RevNum == No):
        return True
    else:
        return False
        
def main():
    Value = int(input("Enter number: "))
    
    Ret = Palindrom(Value)
    
    if(Ret == True):
        print("Palindrom number")
    else:
        print("Non Palindrom number")

if __name__ == "__main__":
    main()