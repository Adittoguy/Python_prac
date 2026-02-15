# Command Line input

import psutil
import sys

Border = "-"*75


def main():
    print(Border)
    print("------------------Marvellous Platform Survillance System-------------------")
    print(Border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to: ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Send mail with the log")
            print("4 : Stores information about processes")
            print("5 : Stores information about CPU")
            print("6 : Stores informations about RAM usage")
            print("7 : Stores information about secondary storage")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("Time Interval    : Time in Minutes for periodic schedulling")
            print("Directory Name   : Name of Directory to create auto logs")
            
        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u for more details")    
        
    # python Demo.py 5 Marvellous    
    elif(len(sys.argv)== 3):
        print("Inside project's logic")
        print("Time Interval    : ", sys.argv[1])
        print("Directory name   : ", sys.argv[2])
    
    else:
        print("Invalid Number of Command Line Arguments")
        print("Unable to procced as there is no such option")
        print("Please use --h or --u for more details")  
    
    print(Border)
    print("----------------------Thank you for using our script-----------------------")
    print(Border)
    
if __name__ == "__main__":
    main()