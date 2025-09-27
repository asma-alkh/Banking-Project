import unittest
from bank.Transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        t = Transaction(1, 10001, "deposit", 50.0, "checking", "checking", 150.0)
        self.assertEqual(t.transaction_id, 1)
        self.assertEqual(t.account_id, 10001)
        self.assertEqual(t.transaction_type, "deposit")
        self.assertEqual(t.amount, 50.0)
        self.assertEqual(t.from_account, "checking")
        self.assertEqual(t.to_account, "checking")
        self.assertEqual(t.balance_after, 150.0)
        self.assertIsNotNone(t.timestamp)
