import unittest
from day11 import power_level, square_power_level, find_largest_fixed_square, find_largest_square


class TestPowerLevel(unittest.TestCase):
    def test_power_level_first_worked_example(self):
        self.assertEqual(4, power_level((3, 5), 8))

    def test_power_level_second_worked_example(self):
        self.assertEqual(-5, power_level((122, 79), 57))

    def test_power_level_third_worked_example(self):
        self.assertEqual(0, power_level((217, 196), 39))

    def test_power_level_forth_worked_example(self):
        self.assertEqual(4, power_level((101, 153), 71))

    def test_power_level_of_square_first_worked_example(self):
        self.assertEqual(29, square_power_level((33, 45), 18, 3))

    def test_power_level_of_square_second_worked_example(self):
        self.assertEqual(30, square_power_level((21, 61), 42, 3))

    def test_find_largest_fixed_square_first_worked_example(self):
        self.assertEqual((33, 45), find_largest_fixed_square(18, 3))

    def test_find_largest_fixed_square_second_worked_example(self):
        self.assertEqual((21, 61), find_largest_fixed_square(42, 3))

    def test_find_largest_square_first_worked_example(self):
        self.assertEqual(((90, 269), 16), find_largest_square(18))

    def test_find_largest_square_second_worked_example(self):
        self.assertEqual(((232, 251), 12), find_largest_square(42))


if __name__ == "__main__":
    unittest.main()
