import unittest
from bank.account import BankAccount  

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Runs before each test - create a new account with initial balance 100
        self.account = BankAccount(account_id=1, balance=100.0)

    def test_deposit(self):
        # Test successful deposit
        success, message = self.account.deposit(50)
        self.assertTrue(success)
        self.assertEqual(message, "Deposit successful")
        self.assertEqual(self.account.get_balance(), 150.0)


    def test_withdraw_success(self):
        # Test successful withdrawal (balance enough)
        success, message = self.account.withdraw(30) 
        self.assertTrue(success)
        self.assertEqual(self.account.get_balance(), 70.0)

    def test_withdraw_fail(self):
         # Test failed withdrawal (exceeds overdraft limit)
        success, message = self.account.withdraw(250)
        self.assertFalse(success)
        self.assertEqual(message, "Withdrawal denied: would exceed overdraft limit")

        def test_overdraft_fee_applied(self):
             # Test overdraft: balance goes negative, fee applied, account still active
            success, message = self.account.withdraw(120)  
            self.assertTrue(success)
             # 100 - 120 = -20, minus overdraft fee (35) => balance = -55
            self.assertEqual(self.account.get_balance(), -55.0)    