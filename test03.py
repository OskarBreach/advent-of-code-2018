import unittest
from day03 import plot_claim, plot_intersection, plot_id, distinct_claims


class PlotClaimTests(unittest.TestCase):
    def test_firstTestCase(self):
        self.assertEqual(plot_claim("#123 @ 3,2: 5x4"),
                        {(3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                         (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                         (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                         (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)})

    def test_secondTestCase(self):
        self.assertEqual(plot_claim("#1 @ 1,3: 4x4"),
                        {(1, 3), (2, 3), (3, 3), (4, 3),
                         (1, 4), (2, 4), (3, 4), (4, 4),
                         (1, 5), (2, 5), (3, 5), (4, 5),
                         (1, 6), (2, 6), (3, 6), (4, 6)})

    def test_thirdTestCase(self):
        self.assertEqual(plot_claim("#2 @ 3,1: 4x4"),
                        {(3, 1), (4, 1), (5, 1), (6, 1),
                         (3, 2), (4, 2), (5, 2), (6, 2),
                         (3, 3), (4, 3), (5, 3), (6, 3),
                         (3, 4), (4, 4), (5, 4), (6, 4)})

    def test_forthTestCase(self):
        self.assertEqual(plot_claim("#3 @ 5,5: 2x2"),
                        {(5, 5), (6, 5),
                         (5, 6), (6, 6)})


class PlotIntersectionTests(unittest.TestCase):
    def setUp(self):
        self.claims = ["#1 @ 1,3: 4x4",
                       "#2 @ 3,1: 4x4",
                       "#3 @ 5,5: 2x2"]

    def tearDown(self):
        self.claims = None

    def test_firstTestCase(self):
        self.assertEqual(plot_intersection(self.claims[0:1]), 0)

    def test_secondTestCase(self):
        self.assertEqual(plot_intersection(self.claims[1:]), 0)

    def test_thirdTestCase(self):
        self.assertEqual(plot_intersection(self.claims[0:3]), 4)

    def test_forthTestCase(self):
        self.assertEqual(plot_intersection(self.claims), 4)


class PlotIdTests(unittest.TestCase):
    def setUp(self):
        self.claims = ["#1 @ 1,3: 4x4",
                       "#2 @ 3,1: 4x4",
                       "#3 @ 5,5: 2x2"]

    def tearDown(self):
        self.claims = None

    def test_firstTestCase(self):
        self.assertEqual(plot_id(self.claims[0]), 1)

    def test_secondTestCase(self):
        self.assertEqual(plot_id(self.claims[1]), 2)

    def test_thirdTestCase(self):
        self.assertEqual(plot_id(self.claims[2]), 3)


class DistinctClaimsTests(unittest.TestCase):
    def setUp(self):
        self.claims = ["#1 @ 1,3: 4x4",
                       "#2 @ 3,1: 4x4",
                       "#3 @ 5,5: 2x2"]

    def tearDown(self):
        self.claims = None

    def test_firstTestCase(self):
        self.assertEqual(distinct_claims(self.claims), [3])


if __name__ == "__main__":
    unittest.main()