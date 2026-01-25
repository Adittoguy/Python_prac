def substraction(A, B):
    return A - B

def Addition(A, B):
    return A + B
    
    
def main():
    No1 = 0
    No2 = 0
    Ans = 0
    
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter Second number: "))
    
    Ans = Addition(No1, No2)
    print("Addition is : ", Ans)
    
    Ans = substraction(No1, No2)
    print("Substraction is : ", Ans)
    
if __name__ == "__main__":
    main()