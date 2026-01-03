def Multiplication(Value1, Value2):
    Ans = None                      # Local Variable
    Ans = Value1 * Value2
    return Ans

print("Demo Application")

No1 = 0
No2 = 0
Result = 0

No1 = int(input("Enter First number: "))
No2 = int(input("Enter Second number: "))

Result  = Multiplication(No1, No2)
print("Multiplication is : ", Result)

#################################################################3

No1 = int(input("Enter First number: "))
No2 = int(input("Enter Second number: "))

Result  = Multiplication(No1, No2)
print("Multiplication is : ", Result)

# def main():
#     print("Enter 1st Number: ")
#     No1 = int(input())

#     print("Enter 2nd Number: ")
#     No2 = int(input())
    
#     iRet = Multiplication(No1, No2)
#     print("Multiplication is : ", iRet)
    
# main()