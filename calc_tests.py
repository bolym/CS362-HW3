import unittest
import calc_app

class TestCase(unittest.TestCase):
    def test_add(self):
            self.assertEqual(calc_app.add(2,2), 4)
            self.assertEqual(calc_app.add(2.0,2.0), 4.0)
            self.assertEqual(calc_app.add(4.0,3.0), 7.0)
            self.assertEqual(calc_app.add(-3,7), 4)

    def test_subtract(self):
            self.assertEqual(calc_app.subtract(2,2), 0)
            self.assertEqual(calc_app.subtract(2.0,2.0), 0.0)
            self.assertEqual(calc_app.subtract(4.0,3.0), 1.0)
            self.assertEqual(calc_app.subtract(-3,7), -10)

    def test_multiply(self):
            self.assertEqual(calc_app.multiply(2,2), 4)
            self.assertEqual(calc_app.multiply(2.0,2.0), 4.0)
            self.assertEqual(calc_app.multiply(4.0,3.0), 12.0)
            self.assertEqual(calc_app.multiply(-3,7), -21)

    def test_divide(self):
            self.assertEqual(calc_app.divide(2,2), 1)
            self.assertEqual(calc_app.divide(2.0,2.0), 1.0)
            self.assertEqual(calc_app.divide(6.0,3.0), 2.0)
            self.assertEqual(calc_app.divide(-4,8), -0.5)
            self.assertEqual(calc_app.divide(3,0), "Cannot divide by 0")


if __name__ == '__main__':
    unittest.main(verbosity=2)