def MinEle(nums):
    min = nums[0]
    
    for i in nums:
        if(min > i):
            min = i
    
    return min

def main():
    data = []
    Value = int(input("Enter Number of Elements: "))
    
    for i in range(Value):
        number = int(input(f"Enter Elements {i + 1} : "))
        data.append(number)
        
    ret = MinEle(data)
    
    print("Min Element in list is : ", ret)
    
if __name__ == "__main__":
    main()