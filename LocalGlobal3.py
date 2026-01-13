
No = 11

def fun():
    No = 21
    print("Value of No from fun is : ", No)     # 11
    No = No + 1
    print("Value of No from fun is : ", No)     # 12


print("Value of No is : ", No)                  # 11

fun()

print("Value of No is : ", No)                  # 12
