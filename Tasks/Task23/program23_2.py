class BankAccount:
    # class variable
    ROI = 10.5

    # constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # display account details
    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    # deposit amount
    def Deposit(self):
        value = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + value
        print("Amount deposited successfully")

    # withdraw amount
    def Withdraw(self):
        value = float(input("Enter amount to withdraw: "))
        if value <= self.Amount:
            self.Amount = self.Amount - value
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    # calculate interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# creating multiple objects
Obj1 = BankAccount("Aditya", 10000)
Obj2 = BankAccount("Rahul", 5000)

# demonstrate methods for first object
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())
print("----------------------------")

# demonstrate methods for second object
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())
