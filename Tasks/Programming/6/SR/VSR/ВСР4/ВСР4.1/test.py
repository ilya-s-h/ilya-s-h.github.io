from main import number_of

if __name__ == '__main__':

    import unittest

    class TestPrecisionFunc(unittest.TestCase):

        def test_numb_type1(self):

            self.assertEqual(number_of(6, ""), "six")


        def test_numb_type2(self):

            self.assertEqual(number_of(7, "bin"), "111")


        def test_numb_type3(self):

            self.assertEqual(number_of(9, "oct"), "11")


        def test_numb_type4(self):

            self.assertEqual(number_of(8, "hex"), "8")


        def test_numb_type5(self):

            self.assertRaises(ValueError, number_of, 3, "fdf")


        def test_numb1(self):

            self.assertEqual(number_of(5), "five")


        def test_numb2(self):

            self.assertRaises(ValueError, number_of, -1)


        def test_numb3(self):

            self.assertRaises(ValueError, number_of, 10)


    unittest.main(verbosity=1)
