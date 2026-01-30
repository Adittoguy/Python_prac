def MaxEle(nums):
    max = nums[0]
    
    for i in nums:
        if(max < i):
            max = i
    
    return max

def main():
    data = []
    Value = int(input("Enter Number of Elements: "))
    
    for i in range(Value):
        number = int(input(f"Enter Elements {i + 1} : "))
        data.append(number)
        
    ret = MaxEle(data)
    
    print("Max Element in list is : ", ret)
    
if __name__ == "__main__":
    main()