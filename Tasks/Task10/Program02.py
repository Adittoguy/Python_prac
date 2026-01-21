def SumOfNNums(No):
    
    sum = 0
    
    for i in range(No + 1):
        sum += i    
    
    return sum

def main():
    Value = int(input("Enter number: "))
    
    Ret = SumOfNNums(Value)
    
    print("Sum of N natural number: ", Ret)
    
if __name__ == "__main__":
    main()