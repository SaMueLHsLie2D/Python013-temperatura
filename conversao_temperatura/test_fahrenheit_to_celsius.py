import unittest
from fahrenheit_to_celsius import fahrenheit_to_celsius


class TestTemperatureConversion(unittest.TestCase):

    def test_positive_temperature(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)

    def test_freezing_point(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)

    def test_negative_temperature(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("abc")


if __name__ == '__main__':
    unittest.main()
