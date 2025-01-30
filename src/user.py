class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)

    def __str__(self):
        return f"User {self.name} with email {self.email}"
