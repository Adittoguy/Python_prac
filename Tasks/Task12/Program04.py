def printSeq(No):
    
    for i in range(1, No + 1):
        print(i)

def main():
    Value = int(input("Enter number: "))
    
    printSeq(Value)
    
if __name__ == "__main__":
    main()