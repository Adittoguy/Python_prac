def ChkPrime(No):
    Count = 0
    
    for i in range(1, No + 1):
        if(No % i == 0):
            Count += 1
            
    if(Count == 2):
        print("It is Prime number")
    else:
        print("It is not prime number")

def main():
    Value = int(input("Enter number : "))
    
    ChkPrime(Value)

if __name__ == "__main__":
    main()