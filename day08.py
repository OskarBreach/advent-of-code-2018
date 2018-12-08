def sum_tree(tree_data):
    if len(tree_data) >= 2 and len(tree_data) >= tree_data[1]:
        subtree_sum = 0
        subtree_start = 2
        subtrees = tree_data[0]

        while subtrees:
            subtree = sum_tree(tree_data[subtree_start:])
            subtree_sum += subtree[0]
            subtree_start += subtree[1]
            subtrees -= 1
        metadata_start = subtree_start
        return subtree_sum + sum(tree_data[metadata_start:metadata_start+tree_data[1]]), \
               metadata_start + tree_data[1]
    else:
        raise Exception("Tree malformed")


def sum_metadata(tree):
    if tree:
        return sum_tree([int(data) for data in tree.split(" ")])[0]
    return 0


def value_tree(tree_data):
    if len(tree_data) >= 2 and len(tree_data) >= tree_data[1]:
        subtree_start = 2
        subtrees = tree_data[0]

        if subtrees == 0:
            return sum_tree(tree_data)

        subtree_values = []
        while subtrees:
            subtree = value_tree(tree_data[subtree_start:])
            subtree_value = subtree[0]
            subtree_start += subtree[1]
            subtree_values.append(subtree_value)
            subtrees -= 1
        metadata_start = subtree_start
        tree_value = 0
        for i in tree_data[metadata_start:metadata_start+tree_data[1]]:
            if i <= len(subtree_values):
                tree_value += subtree_values[i - 1]
        return tree_value, metadata_start + tree_data[1]
    else:
        raise Exception("Tree malformed")


def value(tree):
    if tree:
        return value_tree([int(data) for data in tree.split(" ")])[0]
    return 0


def test1():
    print("Test 1: ")

    with open("inputs/input08.txt", "r") as f:
        tree = f.read()[:-1]
    print(sum_metadata(tree))


def test2():
    print ("Test 2: ")

    with open("inputs/input08.txt", "r") as f:
        tree = f.read()[:-1]
    print(value(tree))


if __name__ == "__main__":
    test1()
    test2()
