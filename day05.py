import re
import string


def resulting_polymer(polymer):
    while True:
        old_len = len(polymer)
        i = 0

        while i < len(polymer) - 1:
            if polymer[i] != polymer[i+1] and polymer[i].upper() == polymer[i+1].upper():
                polymer = polymer[:i] + polymer[i+2:]
            else:
                i += 1

        if len(polymer) == old_len:
            return len(polymer)


def reacted_polymer_after_unit_removed(polymer, unit):
    polymer = re.sub("[" + unit.lower() + unit.upper() + "]", "", polymer)
    return resulting_polymer(polymer)


def shortest_reacted_polymer_after_unit_removed(polymer, units):
    return min(reacted_polymer_after_unit_removed(polymer, unit) for unit in units)


def shortest_reacted_polymer_after_any_unit_removed(polymer):
    return shortest_reacted_polymer_after_unit_removed(polymer, string.ascii_lowercase)


def test1():
    print("Test 1: ")

    with open("inputs/input05.txt", "r") as f:
        polymer = f.read()[:-1]
    print(resulting_polymer(polymer))


def test2():
    print ("Test 2: ")

    with open("inputs/input05.txt", "r") as f:
        polymer = f.read()[:-1]
    print(shortest_reacted_polymer_after_any_unit_removed(polymer))


if __name__ == "__main__":
    test1()
    test2()