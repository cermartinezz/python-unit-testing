import os
from unittest.mock import patch

import pytest

from src.BankAccount import BankAccount
from src.exceptions import OutOfScheduleError


def test_sum():
    a = 3
    b = 3
    assert a + b == 6, "Should be 6"


@pytest.fixture
def account():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    yield account
    if os.path.exists(account.log_file):
        os.remove(account.log_file)


@pytest.mark.parametrize(
    "amount, expected",
    [
        (100, 1100),
        (400, 1400),
        (1000, 2000),
    ],
)
def test_deposit_several_amounts(amount, expected, account):
    new_balance = account.deposit(amount)
    assert new_balance == expected, "Should be 1100, 1400, 2000"


@patch("src.BankAccount.datetime")
def test_withdraw_off_business_days_fails(mock_datetime, account):
    mock_datetime.now.return_value.hour = 9
    mock_datetime.now.return_value.weekday.return_value = 6
    with pytest.raises(OutOfScheduleError):
        account.withdraw(1000)
