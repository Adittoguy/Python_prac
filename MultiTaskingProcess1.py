import multiprocessing
import time
import os

def SumEven(No):
    print("PID of SumEven is : ", os.getpid())                      # Self      51
    print("PPID of SumEven is : ", os.getppid())                    # Main      21
    Sum = 0
    
    for i in range(2, No + 1, 2):
        Sum = Sum + i

    print("Even sum is : ", Sum)
    
def SumOdd(No):
    print("PID of SumOdd is : ", os.getpid())                       # Self      101
    print("PPID of SumOdd is : ", os.getppid())                     # Main      21
    Sum = 0
    
    for i in range(1, No + 1, 2):
        Sum = Sum + i

    print("Odd sum is : ", Sum)
    

def main():
    print("PID of Main is : ", os.getpid())                         # Main      21
    print("PPID of Main is : ", os.getppid())                       # Terminal  11
    
    start_time = time.time()
    
    t1 = multiprocessing.Process(target=SumEven, args=(100000000,))
    t2 = multiprocessing.Process(target=SumOdd, args=(100000000,))
        
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    end_time = time.time()
    
    print("Total Required time : ",end_time - start_time)
    
if __name__ == "__main__":
    main()