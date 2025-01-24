from unittest import TestCase

from src.BankAccount import BankAccount


class BankAccountTests(TestCase):
    def setUp(self):
        self.account = BankAccount(1000)

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
        assert self.account.get_balance() == 500
        assert account2.get_balance() == 1000

    def test_transfer_fail(self):
        with self.assertRaises(ValueError):
            account2 = BankAccount(500)
            self.account.transfer(account2, 2000)
