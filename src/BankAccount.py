from datetime import datetime

from src.exceptions import OutOfScheduleError


class BankAccount:

    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction("Account created")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited {amount}, new balance is {self.balance}")
            return self.balance

        raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        now = datetime.now()

        if now.weekday() > 4 or not (8 <= now.hour <= 17):
            raise OutOfScheduleError()

        if 0 < amount <= self.balance:
            self.balance -= amount
            self.log_transaction(f"Withdrew {amount}, new balance is {self.balance}")
            return self.balance

        raise ValueError("Invalid withdraw amount")

    def get_balance(self):
        return self.balance

    def transfer(self, account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            account.deposit(amount)
            self.log_transaction(f"new Transfer of {amount} succeeded")
            return self.balance

        self.log_transaction(f"new Transfer of {amount}")
        raise ValueError("Invalid transfer amount")

    def log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as file:
                file.write(f"{message}\n")
