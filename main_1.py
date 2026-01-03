def Multiplication(Value1, Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

print("Demo Application for Multiplication of 2 Numbers")

def main():
    No1 = 0
    No2 = 0
    iRet = 0
    
    No1 = int(input("Enter First number: "))
    No2 = int(input("Enter Second number: "))
    
    iRet = Multiplication(No1, No2)
    print("Multiplication is : ", iRet)
    
main()