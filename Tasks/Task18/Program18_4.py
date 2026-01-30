def FreqofELe(nums, no):
    count = 0
    
    for i in nums:
        if(i == no):
            count += 1
            
    return count
    

def main():
    data = []
    Value = int(input("Enter Number of Elements: "))
    
    for i in range(Value):
        number = int(input(f"Enter Elements {i + 1} : "))
        data.append(number)
        
    chk = int(input("Enter number which you want to check: "))
        
    ret = FreqofELe(data, chk)
    
    print("Frequency of Element in list is : ", ret)
    
if __name__ == "__main__":
    main()