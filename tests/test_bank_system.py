import unittest 
from bank.bank_system import BankSystem

class TestBankSystem(unittest.TestCase):

    def setUp(self):
        #Runs before each tese - create a new bank system 
        self.bank = BankSystem()
        #Add a customer with both cheacing and savings accounts 
        self.customer = self.bank.add_customer(
            "John", "Doe", "1234",
            with_checking=True, with_savings=True
        )

    def test_add_customer(self):
         # Test customer added correctly
         self.assertIn(self.customer.account_id, self.bank.customers)
         self.assertEqual(self.customer.first_name, "John")
         self.assertTrue(self.customer.has_checking())
         self.assertTrue(self.customer.has_savings())

    def test_deposit(self):
        # Test deposit updates checking balance
        result = self.bank.deposit(self.customer, "checking", 100.0)
        self.assertTrue(result)
        self.assertEqual(self.customer.checking_account.get_balance(), 100.0)   

    def test_withdraw(self):
        # Test withdraw decrases balance correctly 
        self.bank.deposit(self.customer, "checking", 100.0)
        success, msg = self.bank.withdraw(self.customer, "checking", 50.0)
        self.assertTrue(success)
        self.assertEqual(self.customer.checking_account.get_balance(), 50.0)   


    def test_transfer(self):
        #Test transfer from one customer to another 
        customer2 = self.bank.add_customer(
            "Jane", "Smith", "5678", with_checking=True
        )
        self.bank.deposit(self.customer, "checking", 200.0)
        success, msg = self.bank.transfer(
            self.customer, "checking", customer2, "checking", 100.0
        )
        self.assertTrue(success)
        self.assertEqual(self.customer.checking_account.get_balance(), 100.0)
        self.assertEqual(customer2.checking_account.get_balance(), 100.0)