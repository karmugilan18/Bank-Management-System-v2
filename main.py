from database import Database 
from bank_account import SavingsAccount

db = Database()
db.connect()

print("\n === Loading Account from Database ====")
row = db.get_account("ACC001")

if row:

    account = SavingsAccount(account_id = row[0], account_number= row[1], owner_name= row[4], balance = float(row[3]), interest_rate = 5.0 , db = db)
    account.display_info()

    print("\n=== performing Transaction ===")
    account.deposit(3000)
    account.withdraw(1500)
    account.deposit(500)
    account.add_interest()

    account.show_transaction_history()

else:
    print("Account ACC001 not found")

db.disconnect()
