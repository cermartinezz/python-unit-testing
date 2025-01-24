class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

        raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance

        raise ValueError("Invalid withdraw amount")

    def get_balance(self):
        return self.balance

    def transfer(self, account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            account.deposit(amount)
            return self.balance

        raise ValueError("Invalid transfer amount")
