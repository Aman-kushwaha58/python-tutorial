class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount"

    def get_balance(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

account = BankAccount("Aman kushwaha", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
