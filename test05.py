import unittest

from day05 import resulting_polymer, reacted_polymer_after_unit_removed, shortest_reacted_polymer_after_unit_removed,\
    shortest_reacted_polymer_after_any_unit_removed


class ResultingPolymerTests(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(resulting_polymer("aA"), 0)

    def test_secondTestCase(self):
        self.assertEqual(resulting_polymer("abBA"), 0)

    def test_thirdTestCase(self):
        self.assertEqual(resulting_polymer("abAB"), 4)

    def test_forthTestCase(self):
        self.assertEqual(resulting_polymer("aabAAB"), 6)

    def test_fifthTestCase(self):
        self.assertEqual(resulting_polymer("dabAcCaCBAcCcaDA"), 10)


class RemoveUnitsTests(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "a"), 6)

    def test_secondTestCase(self):
        self.assertEqual(reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "b"), 8)

    def test_thirdTestCase(self):
        self.assertEqual(reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "C"), 4)

    def test_forthTestCase(self):
        self.assertEqual(reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "D"), 6)


class FindShortestRemovedUnitsLength(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(shortest_reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "a"), 6)

    def test_secondTestCase(self):
        self.assertEqual(shortest_reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "B"), 8)

    def test_thirdTestCase(self):
        self.assertEqual(shortest_reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "aB"), 6)

    def test_forthTestCase(self):
        self.assertEqual(shortest_reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "aBc"), 4)

    def test_fifthTestCase(self):
        self.assertEqual(shortest_reacted_polymer_after_unit_removed("dabAcCaCBAcCcaDA", "aBcD"), 4)

    def test_sixthTestCase(self):
        self.assertEqual(shortest_reacted_polymer_after_any_unit_removed("dabAcCaCBAcCcaDA"), 4)


if __name__ == "__main__":
    unittest.main()