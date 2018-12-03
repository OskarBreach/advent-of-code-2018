import itertools


def double_letters(box):
    for c in box:
        if box.count(c) == 2:
            return True
    return False


def triple_letters(box):
    for c in box:
        if box.count(c) == 3:
            return True
    return False


def checksum(boxes):
    doubles = 0
    triples = 0

    for box in boxes:
        if double_letters(box):
            doubles += 1
        if triple_letters(box):
            triples += 1

    return doubles * triples


def num_diffs(lhs, rhs):
    diffs = 0

    for i in range(0, min(len(lhs), len(rhs))):
        if lhs[i] != rhs[i]:
            diffs += 1

    return diffs


def common_elements(lhs, rhs):
    common = ""

    for i in range(0, min(len(lhs), len(rhs))):
        if lhs[i] == rhs[i]:
            common += lhs[i]

    return common


def find_boxes(ids):
    common = ""

    for pair in itertools.combinations(ids, 2):
        if num_diffs(*pair) == 1:
            if common == "":
                common = common_elements(*pair)
            else:
                return ""
    
    return common


def test1():
    print("Test 1: ")

    with open("inputs/input02.txt", "r") as f:
        boxes = f.readlines()
    print(checksum(boxes))


def test2():
    print("Test 2: ")

    with open("inputs/input02.txt", "r") as f:
        boxes = f.readlines()
    print(find_boxes(boxes))


if __name__ == "__main__":
    test1()
    test2()
