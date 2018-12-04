import re
import itertools


def plot_claim(claim):
    claim_search = re.search('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', claim)
    from_left = int(claim_search.group(2))
    from_top = int(claim_search.group(3))
    width = int(claim_search.group(4))
    height = int(claim_search.group(5))

    return set(itertools.product(range(from_left, from_left + width), range(from_top, from_top + height)))


def plot_intersection(claims):
    plot_intersections = []
    for pair in itertools.combinations(claims, 2):
        plot_intersections.append(plot_claim(pair[0]) & plot_claim(pair[1]))

    return len(set().union(*plot_intersections))


def plot_id(claim):
    claim_search = re.search('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', claim)
    return int(claim_search.group(1))


def distinct_claims(claims):
    valid_ids = [plot_id(claim) for claim in claims]

    for pair in itertools.combinations(claims, 2):
        if not plot_claim(pair[0]).isdisjoint(plot_claim(pair[1])):
            if plot_id(pair[0]) in valid_ids:
                valid_ids.remove(plot_id(pair[0]))
            if plot_id(pair[1]) in valid_ids:
                valid_ids.remove(plot_id(pair[1]))

    return valid_ids


def test1():
    print("Test 1: ")

    with open("inputs/input03.txt", "r") as f:
        claims = f.readlines()
    print (plot_intersection(claims))


def test2():
    print("Test 2: ")

    with open("inputs/input03.txt", "r") as f:
        claims = f.readlines()
    print (distinct_claims(claims))


if __name__ == "__main__":
    test1()
    test2()