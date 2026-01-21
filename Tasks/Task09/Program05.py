def Divby3and5(No):
    if(No % 3 == 0 & No % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible")

def main():
    Value = int(input("Enter number: "))
    
    Divby3and5(Value)
    
if __name__ == "__main__":
    main()