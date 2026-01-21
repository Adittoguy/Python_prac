def AreaOfCircle(radius):
    Area = 0
    Area = 3.14 * radius * radius
    return Area

def main():
    Radius = int(input("Enter Radius: "))
    
    Ret = AreaOfCircle(Radius)
    
    print("Area of Circle is : ", Ret)
    
if __name__ == "__main__":
    main()