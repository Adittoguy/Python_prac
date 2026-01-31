import os

def DirectoryScanner(DirectoryName = "Marvellous"):
    
    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("There is no such Directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    
    if(Ret == False):
        print("Unable to scan as it not a directory")
        return
    
    print("Contents of the Directory are: ")

    for FolderName, SubFolderName, FileName in (os.walk(DirectoryName)):
        print("Folder name: ",FolderName)
        
        for subf in SubFolderName:
            print("SubFolderName : ",subf)
            
        for fname in FileName:
            print("File Name : ",fname)

def main():
    DirectoryName = input("Enter the name of directory: ")
    
    DirectoryScanner(DirectoryName)
    
if __name__ == "__main__":
    main()