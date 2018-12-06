import unittest
from day06 import distance, find_closest_coordinate, get_areas, max_area, sum_distance, points_within_bounding_box


class CoordinateTests(unittest.TestCase):
    def setUp(self):
        self.coordinates = [(1, 1),
                            (1, 6),
                            (8, 3),
                            (3, 4),
                            (5, 5),
                            (8, 9)]

    def tearDown(self):
        self.coordinates = None

    def test_distance_between_same_point(self):
        self.assertEqual(distance(self.coordinates[0], self.coordinates[0]), 0)

    def test_distance_between_points_in_line(self):
        self.assertEqual(distance(self.coordinates[0], self.coordinates[1]), 5)

    def test_distance_between_two_distinct_points(self):
        self.assertEqual(distance(self.coordinates[0], self.coordinates[2]), 9)

    def test_distance_is_commutative(self):
        self.assertEqual(distance(self.coordinates[0], self.coordinates[1]),
                         distance(self.coordinates[1], self.coordinates[0]))

    def test_closest_coordinate_empty(self):
        self.assertEqual(find_closest_coordinate(self.coordinates[0], []), None)

    def test_closest_coordinate_self(self):
        self.assertEqual(find_closest_coordinate(self.coordinates[0], [self.coordinates[0]]), self.coordinates[0])

    def test_closest_coordinate_self_in_list(self):
        self.assertEqual(find_closest_coordinate(self.coordinates[0], self.coordinates[0:1]), self.coordinates[0])

    def test_closest_coordinate_equidistant(self):
        self.assertEqual(find_closest_coordinate((2, 2), [(1, 1), (1, 3), (3, 1), (3, 3)]), None)

    def test_closest_coordinate_not_equidistant(self):
        self.assertEqual(find_closest_coordinate((2, 2), [(1, 1), (4, 4)]), (1, 1))

    def test_closest_coordinate_double_point_in_coordinates(self):
        self.assertEqual(find_closest_coordinate((2, 2), [(1, 1), (1, 1), (4, 4)]), (1, 1))

    def test_closest_coordinate_from_test_set(self):
        self.assertEqual(find_closest_coordinate((1, 6), self.coordinates[1:4]), (1, 6))

    def test_area_no_coordinates(self):
        self.assertEqual(get_areas([]), {})

    def test_area_single_coordinate(self):
        self.assertEqual(get_areas([self.coordinates[0]]), {(1, 1): None})

    def test_area_double_coordinates(self):
        self.assertEqual(get_areas(self.coordinates[0:2]), {(1, 1): None, (1, 6): None})

    def test_area_triple_coordinates(self):
        self.assertEqual(get_areas(self.coordinates[1:4]), {(1, 6): None, (8, 3): None, (3, 4): None})

    def test_area_triple_collinear_coordinates(self):
        self.assertEqual(get_areas([(1, 1), (2, 2), (4, 4)]), {(1, 1): None, (2, 2): 3, (4, 4): None})

    def test_total_area(self):
        self.assertEqual(get_areas(self.coordinates), {(1, 1): None,
                                                       (1, 6): None,
                                                       (8, 3): None,
                                                       (3, 4): 9,
                                                       (5, 5): 17,
                                                       (8, 9): None})

    def test_max_area(self):
        self.assertEqual(max_area(self.coordinates), 17)

    def test_sum_distance_inside_bounding_box(self):
        self.assertEqual(sum_distance((4, 3), self.coordinates), 30)

    def test_sum_distance_inside_bounding_box_shifted_up(self):
        self.assertEqual(sum_distance((4, 2), self.coordinates), 34)

    def test_sum_distance_inside_bounding_box_shifted_right(self):
        self.assertEqual(sum_distance((5, 3), self.coordinates), 30)

    def test_sum_distance_inside_bounding_box_shifted_onto_coordinate(self):
        self.assertEqual(sum_distance((3, 4), self.coordinates), 28)

    def test_sum_distance_outside_bounding_box(self):
        self.assertEqual(sum_distance((10, 10), self.coordinates), 66)

    def test_points_within_zero(self):
        self.assertEqual(points_within_bounding_box(0, self.coordinates), 0)

    def test_points_within(self):
        self.assertEqual(points_within_bounding_box(32, self.coordinates), 16)


if __name__ == "__main__":
    unittest.main()