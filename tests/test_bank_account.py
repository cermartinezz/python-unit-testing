import os
from unittest import TestCase

from src.BankAccount import BankAccount


class BankAccountTests(TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def count_lines(self, filename):
        with open(filename, "r") as file:
            return len(file.readlines())

    def test_deposit(self):
        self.account.deposit(500)
        assert self.account.get_balance() == 1500

    def test_withdraw(self):
        self.account.withdraw(500)
        assert self.account.get_balance() == 500

    def test_withdraw_fail(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transfer(self):
        account2 = BankAccount(500)
        self.account.transfer(account2, 500)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(account2.get_balance(), 1000)
        self.assertEqual(self.count_lines(self.account.log_file), 2)

    def test_transfer_fail(self):
        with self.assertRaises(ValueError):
            account2 = BankAccount(500)
            self.account.transfer(account2, 2000)
        self.assertEqual(self.count_lines(self.account.log_file), 2)

    def test_log_transaction(self):
        self.account.deposit(1000)
        assert os.path.exists("transaction_log.txt")

    def test_count_lines_transaction(self):
        assert self.count_lines(self.account.log_file) == 1
        self.account.deposit(1000)
        assert self.count_lines(self.account.log_file) == 2
