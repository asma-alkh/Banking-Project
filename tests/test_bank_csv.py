import unittest 
import csv
import os 

class TestBankCSV(unittest.TestCase):
    def setUp(self):
        self.csv_path = os.path.join(os.path.dirname(__file__), "../bank.csv")

    def test_first_customer_data(self):
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            first_row = next(reader)    

            self.assertEqual(first_row["account_id"], "10001")
            self.assertEqual(first_row["first_name"], "suresh")
            self.assertEqual(first_row["last_name"], "sigera")
            self.assertEqual(float(first_row["balance_checking"]), 1200.0)
            self.assertEqual(float(first_row["balance_savings"]), 10300.0)
      