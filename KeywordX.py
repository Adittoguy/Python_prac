
def EmployeeInfo(Name, Age, salary, city):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", salary)
    print("City : ", city)

def main():
    #Keyword
    EmployeeInfo(Age=25, Name="Rahul", city="Pune", salary= None) # Correct

if __name__ == "__main__":
    main()