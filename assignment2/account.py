class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def check_balance(self):
        return f"Account balance for {self.owner}: ${self.balance}"

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            return f"Transferred ${amount} to {other_account.owner}. Your new balance: ${self.balance}"
        else:
            return "Invalid transfer amount or insufficient balance."

# Create two BankAccount objects
account1 = BankAccount("Ram", 1000.0)
account2 = BankAccount("Raj", 500.0)

# Deposit, withdraw, and check balances
print(account1.deposit(500))
print(account2.deposit(300))
print(account1.withdraw(200))
print(account2.withdraw(100))
print(account1.check_balance())
print(account2.check_balance())

# Transfer money from account1 to account2
print(account1.transfer(account2, 300))

# Check balances after the transfer
print(account1.check_balance())
print(account2.check_balance())
