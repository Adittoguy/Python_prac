
import psutil
import sys
import time
import os 
import schedule

def fun(DirName):
    pass

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
        schedule.every(int(sys.argv[1])).minutes.do(fun,sys.argv[2])

        print("Data Shield System Started succesfully")
        print("Time Interval int minuts:",sys.argv[1])
        print("Pres Ctrl + C to stop the execution")

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