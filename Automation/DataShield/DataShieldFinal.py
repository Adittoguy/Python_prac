
import psutil
import sys
import time
import os 
import schedule
import shutil
import hashlib
import zipfile

Border = "-"*60


def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"
    
    # open the zip file
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)
            
            zobj.write(full_path, relative)
            
    zobj.close()
    
    return zip_name

def calculate_hash(path):
    hobj = hashlib.md5()
    
    fobj = open(path, "rb")
    
    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
            
    fobj.close()
    
    return hobj.hexdigest()

def BackUpFiles(Source, Destination):
    copied_files = []
    
    print("Creating the backup folder for backup process")
    
    os.makedirs(Destination, exist_ok=True)
    
    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)
            
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)
            
            os.makedirs(os.path.dirname(dest_path), exist_ok= True)
            
            # Copy the files if its new 
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)
            
    return copied_files

def DataShieldStart(Source = "Data"):
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Process Started successfully at : ", time.ctime())
    print(Border)    

    files = BackUpFiles(Source, BackupName)
    
    zip_file = make_zip(BackupName)
    
    print("Backup complete successfully")
    print("Files copied : ", len(files))
    print("zip file gets created : ", zip_file)

def main():

    Border = "-"*60
    print(Border)
    print("-------------Marvellous Data Shield System-----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to :")
            print("1 : Takes Auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeINeterval    : The time in minutes for periodic scheduling")
            print("SourceDirectory  : Name of directory to be backed up")

        else:
            print("Unable to proceed as there is no such Option")
            print("Please use --h or --u to get more details ")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projcts logic ")
        print("Time interval        :",sys.argv[1])
        print("SourceDirectory Name :",sys.argv[2])
 
        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(DataShieldStart,sys.argv[2])
    
        print(Border)
        print("Data Shield System Started succesfully")
        print("Time Interval int minuts:",sys.argv[1])
        print("Pres Ctrl + C to stop the execution")
        print(Border)

        # Wait till Abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:   
        print("Invalid Number of command line arguments")
        print("Unable to procede as there is no such Option")
        print("Please use --h or --u to get more details ")

    print(Border)
    print("--------------Thank you for using our script----------------")
    print(Border)

if __name__ == "__main__":
    main()