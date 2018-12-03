import unittest
from day02 import double_letters, triple_letters, checksum, num_diffs, find_boxes


class ResultingFrequencyTests(unittest.TestCase):
    def setUp(self):
        self.testIDs = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

    def test_firstTestCase(self):
        self.assertEqual(double_letters(self.testIDs[0]), False)
        self.assertEqual(triple_letters(self.testIDs[0]), False)

    def test_secondTestCase(self):
        self.assertEqual(double_letters(self.testIDs[1]), True)
        self.assertEqual(triple_letters(self.testIDs[1]), True)

    def test_thirdTestCase(self):
        self.assertEqual(double_letters(self.testIDs[2]), True)
        self.assertEqual(triple_letters(self.testIDs[2]), False)

    def test_forthTestCase(self):
        self.assertEqual(double_letters(self.testIDs[3]), False)
        self.assertEqual(triple_letters(self.testIDs[3]), True)

    def test_fifthTestCase(self):
        self.assertEqual(double_letters(self.testIDs[4]), True)
        self.assertEqual(triple_letters(self.testIDs[4]), False)

    def test_sixthTestCase(self):
        self.assertEqual(double_letters(self.testIDs[5]), True)
        self.assertEqual(triple_letters(self.testIDs[5]), False)

    def test_seventhTestCase(self):
        self.assertEqual(double_letters(self.testIDs[6]), False)
        self.assertEqual(triple_letters(self.testIDs[6]), True)


class ChecksumTests(unittest.TestCase):
    def setUp(self):
        self.testIDs = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

    def test_firstTestCase(self):
        self.assertEqual(checksum(self.testIDs[0]), 0)

    def test_secondTestCase(self):
        self.assertEqual(checksum(self.testIDs[0:2]), 1)

    def test_thirdTestCase(self):
        self.assertEqual(checksum(self.testIDs[0:3]), 2)

    def test_forthTestCase(self):
        self.assertEqual(checksum(self.testIDs[0:4]), 4)

    def test_fifthTestCase(self):
        self.assertEqual(checksum(self.testIDs[0:5]), 6)

    def test_sixthTestCase(self):
        self.assertEqual(checksum(self.testIDs[0:6]), 8)

    def test_seventhTestCase(self):
        self.assertEqual(checksum(self.testIDs), 12)


class NumDifferencesTests(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(num_diffs("abcde", "abcde"), 0)

    def test_secondTestCase(self):
        self.assertEqual(num_diffs("abcdef", "abcdxf"), 1)

    def test_thirdTestCase(self):
        self.assertEqual(num_diffs("abcd", "axcx"), 2)

    def test_forthTestCase(self):
        self.assertEqual(num_diffs("abcdefghij", "xxxxxfghi"), 5)


class FindBoxesTests(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(find_boxes(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]), "fgij")

    def test_secondTestCase(self):
        self.assertEqual(find_boxes([]), "")

    def test_thirdTestCase(self):
        self.assertEqual(find_boxes(["abcde", "fghij", "klmno", "pqrst", "axcye", "wvxyz"]), "")

    def test_forthTestCase(self):
        self.assertEqual(find_boxes(["abcde", "abcde",  "fghij", "klmno", "pqrst", "axcye", "wvxyz"]), "")

    def test_fifthTestCase(self):
        self.assertEqual(find_boxes(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz", "qvxyz"]), "")

    def test_sixthTestCase(self):
        self.assertEqual(find_boxes(["abcde"]), "")


if __name__ == "__main__":
    unittest.main()
