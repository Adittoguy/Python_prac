def sumofele(nums):
    sum = 0
    
    for i in nums:
        sum += i
        
    return sum

def main():
    data = []
    Value = int(input("Enter Number of Elements: "))
    
    for i in range(Value):
        number = int(input(f"Enter Elements {i + 1} : "))
        data.append(number)
        
    ret = sumofele(data)
    
    print("Summation of elements is : ", ret)
    
if __name__ == "__main__":
    main()