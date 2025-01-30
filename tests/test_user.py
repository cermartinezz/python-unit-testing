import os
from unittest import TestCase

from faker import Faker

from src.BankAccount import BankAccount
from src.user import User


class UserTests(TestCase):

    def setUp(self):
        self.faker = Faker(locale="es")
        name = self.faker.name()
        email = self.faker.email()
        self.user = User(name=name, email=email)

    def tearDown(self):
        for account in self.user.accounts:
            os.remove(account.log_file)

    def test_user_creation(self):
        name = self.faker.name()
        email = self.faker.email()
        user = User(name=name, email=email)

        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_user_with_multiple_accounts(self):

        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension="txt"),
            )
            self.user.add_account(bank_account)

        expected_value = self.user.get_total_balance()
        total = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(expected_value, total)
