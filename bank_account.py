class BankAccount:
    """A Class to represent a bank account"""

    def __init__(self , account_number, owner_name,balance =0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def display_info(self):
        print("--------------------------------")
        print(f"Account Number : {self.account_number}")
        print(f"Account Owner  : {self.owner_name} ")
        print(f"Balance        : {self.balance:.2f}")
        print("----------------------------------")

    def deposit (self, amount):
        if amount<=0:
            print (" Deposit amount must be greater than zero ")
            return 
        self.balance += amount 
        print(f"₹{amount:.2f} deposited successfully")
        print(f" New Balance : ₹{self.balance:.2f} ")

    def withdraw (self, amount):
        if amount<=0:
            print (" Withdraw amount must be greater than zero ")
            return 
        if amount> self.balance:
            print("Insufficient Funds")
            print (f" Available Balance  ₹{self.balance:.2f}")
            return 
        self.balance -= amount

        print(f"₹{amount:.2f} withdrawn succesfully.")
        print (f"  New Balance  ₹{self.balance:.2f}")
        
    def check_balance(self):
        print(f"Current Balance for {self.owner_name} :₹{self.balance:.2f} ")

#--- Testing all Methods ---
account1 = BankAccount ("ACC01", "Karmugilan" , 5000.0)
#account2 = BankAccount("ACC002" , "Priya" , 12000.0)

account1.display_info()
 #account2.display_info()

print("\n === Deposit Tests ====")
account1.deposit(2000)
account1.deposit(-500)
account1.deposit(0)

print("\n === Withdraw tests ===")
account1.withdraw(1000)
account1.withdraw(9999)
account1.withdraw(-200)

print("\n ==== Balance Tests ===")
account1.check_balance()


