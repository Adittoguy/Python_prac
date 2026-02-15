
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
    try:
        FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
        print("Log File gets created with Name : ",FileName)
    except:
        pass

    fobj = open(FileName,"w")

    fobj.write(Border +"\n")
    fobj.write("----------Marvellous Platform Serveillence System-----------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border +"\n\n")

    fobj.write("------------------------System Report-----------------------\n")

    # print("CPU Usage :",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n"% psutil.cpu_percent())
    fobj.write(Border +"\n")

    mem = psutil.virtual_memory()
    # print("RAM Usage :",mem.percent)
    fobj.write("RAM Usage : %s %%\n"% mem.percent)
    fobj.write(Border +"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border +"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %%  used \n"%(part.mountpoint ,usage.percent))
        except:
            pass
    fobj.write(Border +"\n")

    net = psutil.net_io_counters()
    fobj.write("\nNetwork usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent /(1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv /(1024 * 1024)))
    fobj.write(Border +"\n")

    # Process Log

    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("UserName : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start_time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border +"\n")




    fobj.write(Border +"\n")
    fobj.write("----------------------- End of Log File --------------------\n")
    fobj.write(Border +"\n")

def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    
    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs = ["pid","name", "username", "status","create_time"])
            # convert create_time
            try: 
                info["create_time"] = time.strftime("%Y-%m-%d:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            listprocess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

        # print(info["pid"],info["username"], info["name"],info["status"])

    return listprocess

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