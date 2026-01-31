
def main():
    try:
        fobj = open("Hello.txt", "w") 
        print("File gets successfully opened")
        
        fobj.write("Jay Ganesh...")
        
        fobj.close()
        
    except FileNotFoundError:
        print("Unable to open file as there is no such file")
        
    finally:
        print("End of Application")
    
if __name__ == "__main__":
    main()