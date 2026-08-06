class BankAccount:
    """A class to represent a bank account — now connected to MySQL."""

    def __init__(self, account_id, account_number, owner_name, balance=0.0, db=None):
        self.account_id = account_id
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.db = db  # Database object injected from outside

    def display_info(self):
        print("-----------------------------")
        print(f"Account Number : {self.account_number}")
        print(f"Account Owner  : {self.owner_name}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("-----------------------------")

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"✅ ₹{amount:.2f} deposited successfully.")
        print(f"   New Balance: ₹{self.balance:.2f}")

        # Save to database if connected
        if self.db:
            self.db.update_balance(self.account_number, self.balance)
            self.db.log_transaction(self.account_id, "deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("❌ Insufficient funds.")
            print(f"   Available Balance: ₹{self.balance:.2f}")
            return
        self.balance -= amount
        print(f"✅ ₹{amount:.2f} withdrawn successfully.")
        print(f"   New Balance: ₹{self.balance:.2f}")

        # Save to database if connected
        if self.db:
            self.db.update_balance(self.account_number, self.balance)
            self.db.log_transaction(self.account_id, "withdrawal", amount)

    def check_balance(self):
        print(f"💰 Current Balance for {self.owner_name}: ₹{self.balance:.2f}")

    def show_transaction_history(self):
        if not self.db:
            print("❌ No database connected.")
            return
        history = self.db.get_transaction_history(self.account_number)
        if not history:
            print("No transactions found.")
            return
        print(f"\n{'─'*55}")
        print(f"  Transaction History for {self.owner_name} ({self.account_number})")
        print(f"{'─'*55}")
        print(f"  {'#':<5} {'Type':<12} {'Amount':>10}  {'Date & Time'}")
        print(f"{'─'*55}")
        for i, row in enumerate(history, 1):
            txn_id   = row[0]
            txn_type = row[1].capitalize()
            amount   = row[2]
            ts       = row[3]
            symbol   = "⬆️ " if txn_type == "Deposit" else "⬇️ "
            print(f"  {i:<5} {symbol}{txn_type:<10} ₹{amount:>9.2f}  {ts}")
        print(f"{'─'*55}\n")


class SavingsAccount(BankAccount):
    """Inherits BankAccount. Adds interest rate feature."""

    def __init__(self, account_id, account_number, owner_name,
                 balance=0.0, interest_rate=4.0, db=None):
        super().__init__(account_id, account_number, owner_name, balance, db)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"✅ Interest of ₹{interest:.2f} added at {self.interest_rate}%.")
        print(f"   New Balance: ₹{self.balance:.2f}")
        if self.db:
            self.db.update_balance(self.account_number, self.balance)
            self.db.log_transaction(self.account_id, "deposit", interest)

    def display_info(self):
        super().display_info()
        print(f"   Interest Rate  : {self.interest_rate}%")
        print("-----------------------------")


class CurrentAccount(BankAccount):
    """Inherits BankAccount. Allows overdraft up to a limit."""

    def __init__(self, account_id, account_number, owner_name,
                 balance=0.0, overdraft_limit=10000.0, db=None):
        super().__init__(account_id, account_number, owner_name, balance, db)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance + self.overdraft_limit:
            print("❌ Overdraft limit exceeded.")
            print(f"   Available (with overdraft): ₹{self.balance + self.overdraft_limit:.2f}")
            return
        self.balance -= amount
        if self.balance < 0:
            print(f"⚠️  ₹{amount:.2f} withdrawn. Account is in overdraft!")
        else:
            print(f"✅ ₹{amount:.2f} withdrawn successfully.")
        print(f"   New Balance: ₹{self.balance:.2f}")
        if self.db:
            self.db.update_balance(self.account_number, self.balance)
            self.db.log_transaction(self.account_id, "withdrawal", amount)

    def display_info(self):
        super().display_info()
        print(f"   Overdraft Limit: ₹{self.overdraft_limit:.2f}")
        print("-----------------------------")