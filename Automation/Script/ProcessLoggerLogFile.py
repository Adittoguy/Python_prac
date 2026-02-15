# Command line Input

import psutil
import sys
import time
import os 

def CreateLog(FolderName):
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")

def main():
    Border = "-"*60
    print(Border)
    print("----------Marvellous Platform Serveillence System-----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to :")
            print("1 : Create automatic logs ")
            print("2 : Executes peridically")
            print("3 : Send mail with the log ")
            print("4 : Store information about Process")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about Secondary Storage")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeINeterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name if directory to create auto logs ")

        else:
            print("Unable to procede as there is no such Option")
            print("Please use --h or --u to get more details ")
    
    # python Demp.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("In side projcts logic ")
        print("Time interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])
        CreateLog(sys.argv[2])

    else:   
        print("Invalid Number of command line arguments")
        print("Unable to procede as there is no such Option")
        print("Please use --h or --u to get more details ")

    print(Border)
    print("--------------Thank you for using our script----------------")
    print(Border)

if __name__ == "__main__":
    main()