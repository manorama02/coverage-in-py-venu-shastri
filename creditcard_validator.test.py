import unittest
import creditcard_validator

class CreditcardValidatorTests(unittest.TestCase):
	def given_emptyCCnumber_expected_false(self):
		self.assertFalse(creditcard_validator.is_valid(""))
	
	def given_CCnumber_less_than_16_expected_false(self):
		self.assertFalse(creditcard_validator.is_valid("12345"))

	def given_CCnumber_more_than_16_expected_false(self):
		self.assertFalse(creditcard_validator.is_valid("123456789012345678"))
	
	def given_incorrect_CCnumber_expected_false(self):
		self.assertFalse(creditcard_validator.is_valid("4012888888881889"))

	def given_correct_CCnumber_expected_true(self):
		self.assertTrue(creditcard_validator.is_valid("4012888888881881"))

if __name__ == "__main__":
	unittest.main()
