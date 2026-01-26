def Chk5Div(No):
    if(No % 5 == 0):
        print("True")
    else:
        print("False")

def main():
    Value = int(input("Enter number: "))
    
    Chk5Div(Value)
    
if __name__ == "__main__":
    main()