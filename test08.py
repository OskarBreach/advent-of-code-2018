import unittest
from day08 import sum_metadata, value


class TestTreeChecks(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(sum_metadata(""), 0)

    def test_single_basic_tree(self):
        self.assertEqual(sum_metadata("0 1 1"), 1)

    def test_single_complex_tree(self):
        self.assertEqual(sum_metadata("0 5 1 2 3 4 5"), 15)

    def test_single_tree_too_large(self):
        self.assertEqual(sum_metadata("0 2 1 2 3 4"), 3)

    def test_single_tree_too_small(self):
        with self.assertRaises(Exception) as context:
            sum_metadata("0 5 1 2")

        self.assertTrue("Tree malformed" in str(context.exception))

    def test_double_basic_trees(self):
        self.assertEqual(sum_metadata("1 1 0 1 2 1"), 3)

    def test_tree_with_multiple_nodes(self):
        self.assertEqual(sum_metadata("3 1 0 1 1 0 1 2 0 1 3 4"), 10)

    def test_worked_example(self):
        self.assertEqual(sum_metadata("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"), 138)

    def test_value_empty_tree(self):
        self.assertEqual(value(""), 0)

    def test_value_single_basic_tree(self):
        self.assertEqual(value("0 1 1"), 1)

    def test_value_single_complex_tree(self):
        self.assertEqual(value("0 5 1 2 3 4 5"), 15)

    def test_value_single_tree_too_large(self):
        self.assertEqual(value("0 2 1 2 3 4"), 3)

    def test_value_single_tree_too_small(self):
        with self.assertRaises(Exception) as context:
            value("0 5 1 2")

        self.assertTrue("Tree malformed" in str(context.exception))

    def test_double_basic_trees(self):
        self.assertEqual(value("1 1 0 1 2 1"), 2)

    def test_value_worked_example(self):
        self.assertEqual(value("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"), 66)


if __name__ == "__main__":
    unittest.main()
