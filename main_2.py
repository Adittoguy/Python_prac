def Multiplication(Value1, Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

def main():
    No1 = 0
    No2 = 0
    iRet = 0
    
    No1 = int(input("Enter First number: "))
    No2 = int(input("Enter Second number: "))
    
    iRet = Multiplication(No1, No2)
    print("Multiplication is : ", iRet)
    
#Starter
if __name__ == "__main__":
    main()
    