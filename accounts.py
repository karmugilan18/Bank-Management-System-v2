from bank_account import BankAccount

#Child Class 1
class SavingsAccount(BankAccount):
    """Inherits bankaccount . Adds interest rate feature"""

    def __init__(self, account_number , owner_name , balance= 0.0 , interest_rate = 4.0):
        super().__init__(account_number , owner_name , balance ) # call parent __init__
        self.interest_rate = interest_rate      # new attribute only Savings Account has

    def add_interest(self):
        interest = self.balance*(self.interest_rate/100)
        self.balance += interest
        print (f"Interest of ₹{interest:.2f} added at {self.interest_rate}% rate.  ")
        print(f" New Balance: ₹{self.balance:.2f}")

    def display_info(self):
        super().display_info() #reuse parent's display_info
        print(f"Interest Rate : {self.interest_rate}%")
        print(f"--------------------------------")

#child class 2
class CurrentAccount(BankAccount):
    """Inherits BankAccount .Allows overdrift up a limit"""

    def __init__(self, account_number , owner_name ,balance =0.0, overdraft_limit = 10000.0):
        super().__init__(account_number , owner_name , balance )
        self.overdraft_limit = overdraft_limit #how much they can go bleow zero

    def withdraw(self, amount):
        if amount <=0:
            print ("Withdrawal amount must be greater than zero.")
            return 
        if amount> self.balance+self.overdraft_limit:
            print(" OverDraft limit execeeded.")
            print(f"Available (with overdraft): ₹{self.balance+self.overdraft_limit:.2f}")
            return 
        self.balance    -=amount
        if self.balance <0:
            print(f"₹{amount:.2f} withdrawn Account is in overdraft!")
        else:
            print("₹{amount:.2f} withdrawn successfully.")
        print(f"New Balance : ₹{self.balance:.2f}")

    def display_info(self):
        super().display_info()
        print(f" Overdraft Limit : ₹{self.overdraft_limit:.2f}")
        print("---------------------------------")

#testing
print("===== Savings Account =====")
savings = SavingsAccount("SAV001" , "Karmugilan", 1000.0  , interest_rate=5.0)
savings.display_info()
savings.deposit(2000)
savings.add_interest()
savings.withdraw(500)

print("\n========== CURRENT ACCOUNT ==========")
current = CurrentAccount("CUR001", "Priya", 5000.0, overdraft_limit=8000.0)
current.display_info()
current.withdraw(3000)   # normal withdraw
current.withdraw(9000)   # uses overdraft
current.withdraw(99999)

print("\n==== isinstance() CHECK====")
print (f"savings is a BankAccount? {isinstance(savings,BankAccount)}")
print(f"current is a BankAccount? {isinstance(current , BankAccount)}")
print(f"savings is a CurrentAccount? {isinstance(savings, CurrentAccount)}")