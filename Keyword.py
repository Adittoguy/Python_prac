
def EmployeeInfo(Name, Age, salary, city):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", salary)
    print("City : ", city)

def main():
    # Positional
    # EmployeeInfo("Rahul", 25, 2000.50, "Pune")  # Correct
    # EmployeeInfo(25, "Rahul", "Pune", 2000.50)  # Wrong
    
    #Keyword
    EmployeeInfo(Age=25, Name="Rahul", city="Pune", salary= 2000.50) # Correct

if __name__ == "__main__":
    main()