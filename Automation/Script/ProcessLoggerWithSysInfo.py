
import psutil
import sys
import time
import os 
import schedule

def CreateLog(FolderName):
    Border = "-"*60
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
            
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log File gets created with Name : ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border +"\n")
    fobj.write("----------Marvellous Platform Serveillence System-----------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border +"\n\n")
    
    fobj.write("---------------------System Report---------------------------\n")
    
    # print("CPU usage : ", psutil.cpu_percent())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    
    fobj.write(Border +"\n")
    
    mem = psutil.virtual_memory()
    # print("RAM usage : ", mem.percent)
    fobj.write("RAM usage : %s %%\n" %mem.percent)
    
    fobj.write(Border +"\n")
    
    fobj.write("\nDisk usage report\n")
    fobj.write(Border +"\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n"%(part.mountpoint, usage.percent))
            
        except:
            pass
    fobj.write(Border +"\n")
        
    net = psutil.net_io_counters()
    fobj.write("\nNetwork usage report\n")
    fobj.write("Sent : %.2fMB\n"%(net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2fMB\n"%(net.bytes_recv / (1024 * 1024)))
    fobj.write(Border +"\n")

    # Process Log

    fobj.write(Border +"\n")
    fobj.write("------------------------ End of Log File ---------------------\n")
    fobj.write(Border +"\n")
    

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
        print("Inside projcts logic ")
        print("Time interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])
 
        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Serveillence System Started succesfully")
        print("Directry created with name :",sys.argv[2])
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