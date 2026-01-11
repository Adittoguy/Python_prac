# Functional Approach

# def CheckEven(No):
#     return(No % 2 == 0)

CheckEven = lambda No:(No % 2 == 0)
        
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