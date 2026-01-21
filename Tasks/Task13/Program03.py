def Perfect(No):
    sum = 0
    
    for i in range(1, No):
        if(No % i == 0):
            sum += i
            
    if(sum == No):
        return True
    else:
        return False

def main():
    Value = int(input("Enter number: "))
    
    Ret = Perfect(Value)
    
    if(Ret == True):
        print("Perfect Number")
    else:
        print("Non Perfect Number")
    
if __name__ == "__main__":
    main()