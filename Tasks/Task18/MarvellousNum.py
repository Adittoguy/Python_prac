def ChkPrime(nums):
    count = 0
    primelist = []
    
    for i in nums:
        for j in range(1, i):
            if(i % j == 0):
                count += 1
        if(count == 1):
            primelist.append(i)
    
    print(primelist)
            
