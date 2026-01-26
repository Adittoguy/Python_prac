def Add(No1, No2):
    sum = 0
    sum = No1 + No2
    return sum   

def main():
    Value1 = int(input("Enter first Number : "))
    Value2 = int(input("Enter second Number : "))
    
    ret = Add(Value1, Value2)
    
    print("Addition is : ", ret)
    
if __name__ == "__main__":
    main()