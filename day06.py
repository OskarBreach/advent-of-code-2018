from collections import namedtuple
from operator import itemgetter
from itertools import product
import re

BoundingBox = namedtuple("BoundingBox", "left top right bottom")


def distance(coordinate1, coordinate2):
    return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])


def get_bounding_box(coordinates):
    return BoundingBox(min(coordinates, key=itemgetter(0))[0],
                       min(coordinates, key=itemgetter(1))[1],
                       max(coordinates, key=itemgetter(0))[0],
                       max(coordinates, key=itemgetter(1))[1])


def get_calculation_area(coordinates):
    if coordinates:
        bounding_box = get_bounding_box(coordinates)
        return set(product(range(bounding_box.left, bounding_box.right + 1),
                           range(bounding_box.top, bounding_box.bottom + 1)))

    return set()


def get_finite_area(coordinates):
    if coordinates:
        bounding_box = get_bounding_box(coordinates)

        if bounding_box.right <= bounding_box.left + 1 or bounding_box.bottom <= bounding_box.top + 1:
            return set()

        return set(product(range(bounding_box.left + 1, bounding_box.right),
                           range(bounding_box.top + 1, bounding_box.bottom)))

    return set()


def get_infinite_area(coordinates):
    return get_calculation_area(coordinates) - get_finite_area(coordinates)


def find_closest_coordinate(point, coordinates):
    coordinate_distance = {}
    for coordinate in coordinates:
        coordinate_distance[coordinate] = distance(point, coordinate)

    closest_points = [k for k,v in coordinate_distance.items()
                      if v == coordinate_distance[min(coordinate_distance, key=coordinate_distance.get)]]
    if len(closest_points) == 1:
        return closest_points[0]

    return None


def get_areas(coordinates):
    areas = {}
    for coordinate in coordinates:
        areas[coordinate] = 0

    closest_coordinates = {}
    calculation_area = get_calculation_area(coordinates)
    for point in get_calculation_area(calculation_area):
        closest_coordinate = find_closest_coordinate(point, coordinates)
        closest_coordinates[point] = closest_coordinate
        if closest_coordinate:
            areas[closest_coordinate] += 1

    infinite_area = get_infinite_area(coordinates)
    for point in infinite_area:
        closest_coordinate = closest_coordinates[point]
        if closest_coordinate:
            areas[closest_coordinate] = None

    return areas


def max_area(coordinates):
    areas = get_areas(coordinates)
    biggest_area = None
    for area in areas:
        if areas[area]:
            if biggest_area is None or areas[area] > biggest_area:
                biggest_area = areas[area]

    return biggest_area


def sum_distance(point, coordinates):
    return sum(distance(point, coordinate) for coordinate in coordinates)


def points_within_bounding_box(region_distance, coordinates):
    region_size = 0
    for point in get_calculation_area(coordinates):
        if sum_distance(point, coordinates) < region_distance:
            region_size += 1

    return region_size


def test1():
    print("Test 1: ")

    coordinates = []
    with open("inputs/input06.txt", "r") as f:
        for line in f:
            coordinate = re.search("([0-9]+), ([0-9]+)", line)
            if coordinate:
                coordinates.append((int(coordinate.group(1)), int(coordinate.group(2))))
    print(max_area(coordinates))


def test2():
    print("Test 2: ")

    coordinates = []
    with open("inputs/input06.txt", "r") as f:
        for line in f:
            coordinate = re.search("([0-9]+), ([0-9]+)", line)
            if coordinate:
                coordinates.append((int(coordinate.group(1)), int(coordinate.group(2))))
    print(points_within_bounding_box(10000, coordinates))


if __name__ == "__main__":
    test1()
    test2()
