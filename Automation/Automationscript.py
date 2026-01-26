import sys

def main():
    Border = "-"*70
    print(Border)
    print("---------------------------- Automation ------------------------------")
    print(Border)
    
    if(len(sys.argv) == 2):
        
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform _____")
            print("This is a Automation script")
            
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument 2")
            print("Argument1 : ____________")
            print("Argument2 : ____________")
            
        else:
            print("Use the given flags as: ")
            print("--u : Used to display the usage")
            print("--h : Used to display the help") 
            
    else:
        print("Invalid number of Command Line")
        print("Use the given flags as: ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help") 
        
    print(Border)
    print("------------------ Thank you for using our script --------------------")
    print(Border)
    
if __name__ == "__main__":
    main()