def Digit(No):
    count = 0
    
    while(No > 0):
        No //= 10
        count += 1
        
    return count
        

def main():
    Value = int(input("Enter number: "))
    
    ret = Digit(Value)
    
    print("Digits in number are: ", ret)
    
if __name__ == "__main__":
    main()