from main import factorial

if __name__ == '__main__':

    import unittest

    class TestPrecisionFunc(unittest.TestCase):
        
        def test_n_is_not_int(self):

            self.assertRaises(TypeError, factorial, 3.14)


        def test_n_less_then_zero(self):

            self.assertRaises(ValueError, factorial, -1)


        def test_n_is_ok(self):

            self.assertEqual(factorial(5), 120)

    unittest.main(verbosity=1)
