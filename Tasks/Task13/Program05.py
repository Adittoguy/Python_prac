def Result(No):
    if(No >= 75):
        print("Distinction")
    elif(No >= 65 and No <= 74):
        print("First Class")
    elif(No >= 50 and No <= 64):
        print("Second Class")
    else:
        print("Fail!")

def main():
    Marks = int(input("Enter marks: "))
    
    Result(Marks)
    
if __name__ == "__main__":
    main()