def TableNo(No):
    for i in range(1, 11):
        print(i * No)

def main():
    Value = int(input("Enter number: "))
    
    TableNo(Value)
    
if __name__ == "__main__":
    main()