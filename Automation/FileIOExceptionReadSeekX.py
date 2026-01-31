# seek(offset, whence)
# offset - 0 / 1 / 2
# 0 : Start
# 1 : Current
# 2 : End

def main():
    try:
        fobj = open("Hello.txt", "r") 
        print("File gets successfully opened")
        
        print("Current offset is : ", fobj.tell())  
        
        fobj.seek(7, 0)
        
        print("Current offset is : ", fobj.tell())  
        
        Data = fobj.read(10)                        
        
        print("Current offset is : ", fobj.tell())  
        
        print("Data from  file is : ", Data)     
                
        fobj.close()
        
    except FileNotFoundError:
        print("Unable to open file as there is no such file")
        
    finally:
        print("End of Application")
    
if __name__ == "__main__":
    main()