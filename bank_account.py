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

account1 = BankAccount ("ACC01", "Karmugilan" , 5000.0)
account2 = BankAccount("ACC002" , "Priya" , 12000.0)

account1.display_info()
account2.display_info()

