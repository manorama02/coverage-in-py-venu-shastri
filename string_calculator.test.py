import unittest
import string_calculator
class String_calculatorTest(unittest.TestCase):
	def given_empty_string_zero_expected(self):
		self.assertTrue(string_calculator.add("") == 0)
	def given_single_value_same_expected(self):
		self.assertTrue(string_calculator.add("2") == 2)
	def test_given_two_values_addition_expected(self):
		self.assertTrue(string_calculator.add("2,3") == 5)
if __name__ == '__main__':
  unittest.main()
