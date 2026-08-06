import mysql.connector
from mysql.connector import Error

class Database:
    """Handles all MySQL connections and queries."""

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="bank_management"
            )
            self.cursor = self.connection.cursor()
            print("Database connected Successfully")
        except Error as e:
            print(f"Connection failed {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database disconnected.")

    # -- Create --
    def add_customer(self, full_name, phone, address):
        try:
            query = """INSERT INTO customers (full_name, phone, address) VALUES (%s, %s, %s)"""
            self.cursor.execute(query, (full_name, phone, address))
            self.connection.commit()
            customer_id = self.cursor.lastrowid
            print(f"Customer added with ID: {customer_id}")
            return customer_id
        except Error as e:
            print(f"Error Adding Customer {e}")
            return None

    def add_account(self, account_number, customer_id, account_type, balance=0.0):
        try:
            query = """INSERT INTO accounts (account_number, customer_id, account_type, balance) VALUES (%s, %s, %s, %s)"""
            self.cursor.execute(query, (account_number, customer_id, account_type, balance))
            self.connection.commit()
            account_id = self.cursor.lastrowid
            print(f"Account created: {account_number}")
            return account_id
        except Error as e:
            print(f"Error Adding account {e}")
            return None

    # -- Read --
    def get_account(self, account_number):
        try:
            query = """SELECT a.account_id, a.account_number, a.account_type, a.balance, c.full_name, c.phone
                       FROM accounts a
                       JOIN customers c ON a.customer_id = c.customer_id
                       WHERE a.account_number = %s"""
            self.cursor.execute(query, (account_number,))
            result = self.cursor.fetchone()
            return result
        except Error as e:
            print(f"Error fetching account {e}")
            return None

    # -- Update --
    def update_balance(self, account_number, new_balance):
        try:
            query = """UPDATE accounts SET balance = %s WHERE account_number = %s"""
            self.cursor.execute(query, (new_balance, account_number))
            self.connection.commit()
            print(f"✅ Balance updated to ₹{new_balance:.2f}")
        except Error as e:
            print(f"Error updating balance: {e}")

    def log_transaction(self, account_id, transaction_type, amount):
        try:
            query = """INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)"""
            self.cursor.execute(query, (account_id, transaction_type, amount))
            self.connection.commit()
        except Error as e:
            print(f"Error logging transaction: {e}")
#--- history --
    def get_transaction_history(self, account_number):
        try:
            query ="""select t.transaction_id , t.transaction_type , t.amount , t.timestamp , a.account_number , c.full_name from transactions t join accounts a on t.account_id = a.account_id join customers c on a.customer_id = c.customer_id where a.account_number = %s order by t.timestamp desc limit 10 """
            self.cursor.execute(query , (account_number ,))
            results = self.cursor.fetchall()
            return results  

        except Error as e:
            print(f"Error fetching transaction history :{e}")
            return []

    def get_account_by_id(self , account_id):
        try:
            query = "select * form accounts where account_id = %s"
            self.cursor.execute(query  , (account_id,))
            return  self.cursor.fetchone()
        except Error as e:
            print(f"Error fetching account by ID : {e}")
            return None
# --- Testing ---
if __name__ == "__main__":
    db = Database()
    db.connect()

    print("\n=== Add New Customer ===")
    customer_id = db.add_customer("Priya", "9123456780", "Coimbatore, TN")

    print("\n=== Add Account for that Customer ===")
    account_id = db.add_account("ACC002", customer_id, "savings", 8000.0)

    print("\n=== Fetch Account Details ===")
    account = db.get_account("ACC002")
    if account:
        print(f"Account ID     : {account[0]}")
        print(f"Account Number : {account[1]}")
        print(f"Account Type   : {account[2]}")
        print(f"Balance        : ₹{account[3]}")
        print(f"Owner Name     : {account[4]}")
        print(f"Phone          : {account[5]}")

    print("\n=== Update Balance ===")
    db.update_balance("ACC002", 9500.0)

    print("\n=== Log a Transaction ===")
    db.log_transaction(account_id, "deposit", 1500.0)

    print("\n=== Verify Updated Account ===")
    account = db.get_account("ACC002")
    if account:
        print(f"New Balance: ₹{account[3]}")

    db.disconnect()