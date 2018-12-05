import re
from collections import namedtuple


Guard = namedtuple("Guard", "id minutes_asleep minute_most_asleep times_asleep_at_favourite_minute")


def get_guard_patterns(records):
    records.sort()

    guard_asleep = {}
    current_guard = None

    for record in records:
        shift_start = re.search(".*Guard #([0-9]+) begins shift", record)
        if shift_start:
            current_guard = int(shift_start.group(1))
            if current_guard not in guard_asleep:
                guard_asleep[current_guard] = [0] * 60
        falls_asleep = re.search(".*00:([0-9]+)\] falls asleep", record)
        if falls_asleep:
            asleep_time = int(falls_asleep.group(1))
            for minute in range(asleep_time, 60):
                guard_asleep[current_guard][minute] += 1
        wakes_up = re.search(".*00:([0-9]+)\] wakes up", record)
        if wakes_up:
            wake_time = int(wakes_up.group(1))
            for minute in range(wake_time, 60):
                guard_asleep[current_guard][minute] -= 1

    guard_pattern = []
    for guard in guard_asleep:
        asleep = guard_asleep[guard]
        time_most_asleep = asleep.index(max(asleep))
        guard_pattern.append(Guard(guard, sum(asleep), time_most_asleep, asleep[time_most_asleep]))

    return guard_pattern


def get_guard_most_asleep(records):
    guards = get_guard_patterns(records)

    guard_most_asleep = None
    for guard in guards:
        if guard_most_asleep is None:
            guard_most_asleep = guard
        elif guard.minutes_asleep > guard_most_asleep.minutes_asleep:
            guard_most_asleep = guard

    return guard_most_asleep


def get_guard_most_frequently_asleep(records):
    guards = get_guard_patterns(records)

    guard_most_frequently_asleep = None
    for guard in guards:
        if guard_most_frequently_asleep is None:
            guard_most_frequently_asleep = guard
        elif guard.times_asleep_at_favourite_minute > guard_most_frequently_asleep.times_asleep_at_favourite_minute:
            guard_most_frequently_asleep = guard

    return guard_most_frequently_asleep


def test1():
    print("Test 1: ")

    with open("inputs/input04.txt", "r") as f:
        records = f.readlines()
    guard = get_guard_most_asleep(records)
    print(guard.id, " (minutes asleep = ", guard.minutes_asleep, "): ", guard.id * guard.minute_most_asleep)


def test2():
    print("Test 2: ")

    with open("inputs/input04.txt", "r") as f:
        records = f.readlines()
    guard = get_guard_most_frequently_asleep(records)
    print(guard.id, " (minutes asleep = ", guard.minutes_asleep, "): ", guard.id * guard.minute_most_asleep)


if __name__ == "__main__":
    test1()
    test2()