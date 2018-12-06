import unittest
import random
from day04 import Guard, get_guard_patterns,get_guard_most_asleep, guard_most_frequently_asleep


class GuardAsleepTests(unittest.TestCase):
    def setUp(self):
        self.records = ["[1518-11-01 00:00] Guard #10 begins shift",
                        "[1518-11-01 00:05] falls asleep",
                        "[1518-11-01 00:25] wakes up",
                        "[1518-11-01 00:30] falls asleep",
                        "[1518-11-01 00:55] wakes up",
                        "[1518-11-01 23:58] Guard #99 begins shift",
                        "[1518-11-02 00:40] falls asleep",
                        "[1518-11-02 00:50] wakes up",
                        "[1518-11-03 00:05] Guard #10 begins shift",
                        "[1518-11-03 00:24] falls asleep",
                        "[1518-11-03 00:29] wakes up",
                        "[1518-11-04 00:02] Guard #99 begins shift",
                        "[1518-11-04 00:36] falls asleep",
                        "[1518-11-04 00:46] wakes up",
                        "[1518-11-05 00:03] Guard #99 begins shift",
                        "[1518-11-05 00:45] falls asleep",
                        "[1518-11-05 00:55] wakes up"]

    def tearDown(self):
        self.records = None

    def test_no_rows(self):
        self.assertEqual(get_guard_patterns([]), [])

    def test_first_rows(self):
        self.assertEqual(get_guard_patterns(self.records[0:1]), [Guard(10, 0, 0, 0)])

    def test_guard_falls_asleep(self):
        self.assertEqual(get_guard_patterns(self.records[0:2]), [Guard(10, 55, 5, 1)])

    def test_guard_falls_asleep_and_wakes(self):
        self.assertEqual(get_guard_patterns(self.records[0:3]), [Guard(10, 20, 5, 1)])

    def test_full_guard_cycle(self):
        self.assertEqual(get_guard_patterns(self.records[0:5]), [Guard(10, 45, 5, 1)])

    def test_two_full_cycles(self):
        self.assertEqual(get_guard_patterns(self.records[0:8]), [Guard(10, 45, 5, 1), Guard(99, 10, 40, 1)])

    def test_full_records(self):
        self.assertEqual(get_guard_patterns(self.records), [Guard(10, 50, 24, 2), Guard(99, 30, 45, 3)])

    def test_scrambled_records(self):
        scrambled_records = self.records
        # deterministic shuffle
        random.Random(4).shuffle(scrambled_records)
        self.assertEqual(get_guard_patterns(scrambled_records), [Guard(10, 50, 24, 2), Guard(99, 30, 45, 3)])

    def test_get_guard_most_asleep_two_cycles(self):
        self.assertEqual(get_guard_most_asleep(self.records[5:11]), Guard(99, 10, 40, 1))

    def test_get_guard_most_asleep_full(self):
        self.assertEqual(get_guard_most_asleep(self.records), Guard(10, 50, 24, 2))

    def test_get_guard_most_frequently_asleep_on_same_minute(self):
        self.assertEqual(get_guard_most_frequently_asleep(self.records), Guard(99, 30, 45, 3))


if __name__ == "__main__":
    unittest.main()

