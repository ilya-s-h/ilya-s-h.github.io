import unittest
import main

class CurrencyInfoTest(unittest.TestCase):
    def test_object_type(self):
        c_info = main.CurrencyInfo()
        self.assertIsInstance(c_info, main.CurrencyInfo)


    def test_instances_ids(self):
        x = main.CurrencyInfo()
        y = main.CurrencyInfo()
        self.assertEqual(id(x), id(y))


    def test_result_type(self):
        c_info = main.CurrencyInfo()
        rates = c_info.get_currencies()
        self.assertIsInstance(rates, dict)