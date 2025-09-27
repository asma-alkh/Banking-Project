import unittest
from bank.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
         # Runs before each test - create a customer with checking (100) and savings (50)
        self.customer = Customer(10001, "John", "Doe", "1234", 100.0, 50.0)

    def test_full_name(self):
        # Test full_name returns "First Last"
        self.assertEqual(self.customer.full_name(), "John Doe")

    def test_get_account_checking(self):
        # Test getting checking account returns correct balance
        acc = self.customer.get_account("checking")
        self.assertIsNotNone(acc)
        self.assertEqual(acc.get_balance(), 100.0)

    def test_get_account_savings(self):
        # Test getting savings account returns correct balance
        acc = self.customer.get_account("savings")
        self.assertIsNotNone(acc)
        self.assertEqual(acc.get_balance(), 50.0)
