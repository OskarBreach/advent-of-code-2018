def resulting_frequency(frequency_changes):
    frequency = 0
    for change in frequency_changes:
        if change[0] == "+":
            frequency += int(change[1:])
        else:
            frequency -= int(change[1:])
    return frequency


def first_repeated_frequency(frequency_changes):
    deltas = []
    for change in frequency_changes:
        if change[0] == "+":
            deltas.append(int(change[1:]))
        else:
            deltas.append(-int(change[1:]))

    frequency = 0
    frequencies = [frequency]
    while True:
        for delta in deltas:
            frequency += delta
            if frequency in frequencies:
                return frequency
            else:
                frequencies.append(frequency)


def test1():
    print("Test 1: ")

    with open("inputs/input 01.txt", "r") as f:
        frequency_changes = f.readlines()
    print(resulting_frequency(frequency_changes))


def test2():
    print("Test 2: ")

    with open("inputs/input 01.txt", "r") as f:
        frequency_changes = f.readlines()
    print(first_repeated_frequency(frequency_changes))


if __name__ == "__main__":
    test1()
    test2()
