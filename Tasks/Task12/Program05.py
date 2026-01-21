def printRevSeq(No):
    
    for i in range(No, 0, -1):
        print(i)

def main():
    Value = int(input("Enter number: "))
    
    printRevSeq(Value)
    
if __name__ == "__main__":
    main()