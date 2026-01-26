def ChkNum(No):
    flag = False
    
    if(No % 2 == 0):
        flag = True 
        
    return flag   

def main():
    Value = int(input("Enter Number : "))
    
    ret = ChkNum(Value)
    
    if(ret == True):
        print("Even Number")
    else:
        print("Odd Number")
    
if __name__ == "__main__":
    main()