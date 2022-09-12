import unittest
import typewise_alert
from unittest.mock import patch

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    
  def test_infer_breach_for_too_high(self):
    self.assertTrue(typewise_alert.infer_breach(200, 50, 100) == 'TOO_HIGH')
    
  def test_infer_breach_for_normal(self):
    self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')#increased coverage from 36 to 41%
    
  def test_classify_temperature_passive_cooling_too_low(self):
     self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -2)== 'TOO_LOW')#increased coverage from 52 to 59%
      
  def test_classify_temperature_passive_cooling_too_high(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 36)== 'TOO_HIGH')#increased coverage from 59 to 60%
    
  def test_classify_temperature_passive_cooling_normal(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 30 )== 'NORMAL')
  
  def test_classify_temperature_hi_active_cooling_too_low(self):
     self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', -2)== 'TOO_LOW')
      
  def test_classify_temperature_hi_active_cooling_too_high(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50)== 'TOO_HIGH')
    
  def test_classify_temperature_hi_active_cooling_normal(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 40 )== 'NORMAL')
  
  #above tests increased coverage from 60 to 65%
  
  def test_classify_temperature_med_active_cooling_too_low(self):
     self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', -2)== 'TOO_LOW')
      
  def test_classify_temperature_med_active_cooling_too_high(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 41)== 'TOO_HIGH')
    
  def test_classify_temperature_med_active_cooling_normal(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 39 )== 'NORMAL')
    #above tests increased coverage from 65 to 68%
@patch('builtins.print')
def test_send_to_controller_too_low(self, mock_print):
	typewise_alert.send_to_controller('TOO_LOW')
	mock_print.assert_called_with(f'{0xfeed}, TOO_LOW')
@patch('builtins.print')
def test_send_to_controller_too_low(self, mock_print):
	typewise_alert.send_to_controller('TOO_HIGH')
	mock_print.assert_called_with(f'{0xfeed}, TOO_HIGH')
@patch('builtins.print')
def test_send_to_email_too_low(self, mock_print):
	typewise_alert.send_to_email('TOO_LOW')
	assert mock_print.mock_calls == [call('To: a.b@c.com'), call('Hello, the temperature is too low')]
@patch('builtins.print')
def test_send_to_email_too_high(self, mock_print):
	typewise_alert.send_to_email('TOO_HIGH')
	assert mock_print.mock_calls == [call('To: a.b@c.com'), call('Hello, the temperature is too high')]

    
     

if __name__ == '__main__':
  unittest.main()
