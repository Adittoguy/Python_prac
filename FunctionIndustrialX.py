
def CheckEven(No):
    Flag = False
    
    if(No % 2 == 0):
        Flag = True
    else:
        Flag = False
    
    return Flag
    
def main():
    Ret = False
    Value = 0
    
    print("Enter number: ")
    Value = int(input())
    
    Ret = CheckEven(Value)
    print(Ret)
    
    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")

    
if __name__ == "__main__":
    main()