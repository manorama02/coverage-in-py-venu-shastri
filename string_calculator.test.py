import unittest

class String_calculatorTest(unittest.TestCase):
  def given_empty_string_zero_expected(self):
    self.assertTrue(add("0") == 0)
  



if __name__ == '__main__':
  unittest.main()
