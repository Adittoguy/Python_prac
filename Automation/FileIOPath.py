import os

def main():
    FileName = input("Enter the name of File: ")
    
    Ret = os.path.isabs(FileName)
    
    if(Ret == True):
        print('It is Absolute path')
        
    else:
        print("It is relative path")
    
    
if __name__ == "__main__":
    main()