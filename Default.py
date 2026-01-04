
def EmployeeInfo(Name = "Gotya", Age = 21, salary = 1000, city = "Mumbai"):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", salary)
    print("City : ", city)

def main():
    EmployeeInfo(Age=25, Name="Rahul", salary= None ,city="Pune") # Correct
    EmployeeInfo()

if __name__ == "__main__":
    main()