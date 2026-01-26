def ChkPrime(No):
    count = 0
    
    for i in range(1, No):
        if(No % i == 0):
            count += 1
            
    if(count == 1):
        return True
    else:
        return False


def main():
    Value = int(input("Enter number: "))
    
    ret = ChkPrime(Value)
    
    if(ret == True):
        print("Prime Number")
    else:
        print("Non Prime number")
    
if __name__ == "__main__":
    main()