def Sqrt(No):
    sq = 0
    sq = No * No
    return sq

def main():
    Value = int(input("Enter number: "))
    Ret = Sqrt(Value)
    
    print("Square of ",Value," is ", Ret) 
    
if __name__ == "__main__":
    main()