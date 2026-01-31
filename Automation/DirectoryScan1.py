import os

def main():
    DirectoryName = input("Enter the name of directory: ")
    
    print("Contents of the DIrectory are: ")
    
    for FolderName, SubFolderName, FileName in (os.walk(DirectoryName)):
        print("Folder name: ",FolderName)
        
        for subf in SubFolderName:
            print("SubFolderName : ",subf)
            
        for fname in FileName:
            print("File Name : ",fname)
    
if __name__ == "__main__":
    main()