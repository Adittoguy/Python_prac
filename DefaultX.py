
def EmployeeInfo(Name, Age, salary, city = "Mumbai"):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", salary)
    print("City : ", city)

def main():
    EmployeeInfo("Rahul", 25, 2000.50)
    EmployeeInfo("Rahul", 25, 2000.50, "Pune")

if __name__ == "__main__":
    main()