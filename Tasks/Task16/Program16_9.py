def Display():
    count = 0
    num = 2
    
    while count < 10:
        print(num, end='\t')
        num += 2
        count += 1
        
    print('\n')

def main():  
    Display()
    
if __name__ == "__main__":
    main()