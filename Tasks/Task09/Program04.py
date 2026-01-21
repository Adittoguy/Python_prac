def Cbrt(No):
    cb = 0
    cb = No * No * No
    return cb

def main():
    Value = int(input("Enter number: "))
    Ret = Cbrt(Value)
    
    print("Cube of ",Value," is ", Ret) 
    
if __name__ == "__main__":
    main()