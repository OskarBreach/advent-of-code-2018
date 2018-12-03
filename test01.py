import unittest
from day01 import resulting_frequency, first_repeated_frequency


class ResultingFrequencyTests(unittest.TestCase):

    def test_firstTestCase(self):
        self.assertEqual(resulting_frequency(["+1", "+1", "+1"]), 3)

    def test_secondTestCase(self):
        self.assertEqual(resulting_frequency(["+1", "+1", "-2"]), 0)

    def test_thirdTestCase(self):
        self.assertEqual(resulting_frequency(["-1", "-2", "-3"]), -6)


class RepeatedFrequencyTests(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(first_repeated_frequency(["+1", "-1"]), 0)

    def test_secondTestCase(self):
        self.assertEqual(first_repeated_frequency(["+3", "+3", "+4", "-2", "-4"]), 10)

    def test_thirdTestCase(self):
        self.assertEqual(first_repeated_frequency(["-6", "+3", "+8", "+5", "-6"]), 5)

    def test_forthTestCase(self):
        self.assertEqual(first_repeated_frequency(["+7", "+7", "-2", "-7", "-4"]), 14)


if __name__ == "__main__":
    unittest.main()
