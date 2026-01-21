def AreaOfRec(No1, No2):
    Area = 0
    Area = No1 * No2
    return Area

def main():
    width = int(input("Enter Width: "))
    height = int(input("Enter height: "))
    
    Ret = AreaOfRec(width, height)
    
    print("Area of Rectangle is : ", Ret)
    
if __name__ == "__main__":
    main()