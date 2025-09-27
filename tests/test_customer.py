import unittest
from bank.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        # Runs before each test - create a new account with initial balance 100
        self.account = Account(100.0)

    def test_deposit(self):
        # Test successful deposit
        result = self.account.deposit(50)
        self.assertTrue(result)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_withdraw_success(self):
        # Test successful withdrawal (balance enough)
        success, message = self.account.withdraw(30)
        self.assertTrue(success)
        self.assertEqual(self.account.get_balance(), 70.0)

    def test_withdraw_fail(self):
        # Test failed withdrawal (balance not enough)
        success, message = self.account.withdraw(200)
        self.assertFalse(success)
        self.assertEqual(message, "Insufficient funds.")
