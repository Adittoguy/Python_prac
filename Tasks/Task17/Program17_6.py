def Display(No):
    
    for i in range(No, 0, -1):
        for j in range(1, i + 1):
            print('*', end='\t')
        
        print(" ")

def main():
    Value = int(input("Enter number: "))
    
    Display(Value)
    
if __name__ == "__main__":
    main()