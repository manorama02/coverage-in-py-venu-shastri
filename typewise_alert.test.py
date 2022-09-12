import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    
  def test_infer_breach_for_too_high(self):
    self.assertTrue(typewise_alert.infer_breach(200, 50, 100) == 'TOO_HIGH')
    
  def test_infer_breach_for_normal(self):
    self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')#increased coverage from 36 to 41%
    
  def test_classify_temperature(self):
     self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -2)== 'TOO_LOW')
    
   
 

if __name__ == '__main__':
  unittest.main()
