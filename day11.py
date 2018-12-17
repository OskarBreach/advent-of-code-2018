def power_level(coordinate, grid_serial_number):
    rack_id = coordinate[0] + 10
    ret = rack_id * coordinate[1]
    ret += grid_serial_number
    ret *= rack_id
    ret //= 100
    ret %= 10
    ret -= 5

    return ret


def find_sum_power_levels(grid_serial_number):
    sum_power_levels = {(x, 301): 0 for x in range(0, 302)}
    for y in range(0, 302):
        sum_power_levels[(301, y)] = 0

    for x in range(300, -1, -1):
        for y in range(300, -1, -1):
            sum_power_levels[(x, y)] = power_level((x, y), grid_serial_number) \
                                       + sum_power_levels[(x + 1, y)] \
                                       + sum_power_levels[(x, y + 1)] \
                                       - sum_power_levels[(x + 1, y + 1)]

    return sum_power_levels


def square_power_level(coordinate, size, sum_power_levels):
    return sum_power_levels[(coordinate[0], coordinate[1])]\
           - sum_power_levels[(coordinate[0] + size, coordinate[1])]\
           - sum_power_levels[(coordinate[0], coordinate[1] + size)]\
           + sum_power_levels[(coordinate[0] + size, coordinate[1] + size)]


def find_largest_fixed_square(grid_serial_number, size):
    sum_power_levels = find_sum_power_levels(grid_serial_number)

    all_squares = {(x, y): square_power_level((x, y), size, sum_power_levels)
                   for x in range(0, 300 - size)
                   for y in range(0, 300 - size)}

    return max(all_squares, key=all_squares.get)


def find_largest_square(grid_serial_number):
    sum_power_levels = find_sum_power_levels(grid_serial_number)

    largest = (0, 0), 1
    for size in range(1, 301):
        for x in range(0, 300 - size):
            for y in range(0, 300 - size):
                if square_power_level((x, y), size, sum_power_levels) > square_power_level(*largest, sum_power_levels):
                    largest = ((x, y), size)

    return largest


def test1():
    print("Test 1: ")

    with open("inputs/input11.txt", "r") as f:
        grid_serial_number = int(f.read()[:-1])
    print(find_largest_fixed_square(grid_serial_number, 3))


def test2():
    print("Test 2: ")

    with open("inputs/input11.txt", "r") as f:
        grid_serial_number = int(f.read()[:-1])
    print(find_largest_square(grid_serial_number))


if __name__ == "__main__":
    test1()
    test2()