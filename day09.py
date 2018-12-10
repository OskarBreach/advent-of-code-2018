import re
from collections import deque


def get_high_score(game):
    game_inputs = re.search("([0-9]+) players; last marble is worth ([0-9]+) points", game)
    if game_inputs:
        players = int(game_inputs.group(1))
        last_marble = int(game_inputs.group(2))

        marbles = deque([0])
        high_score = [0] * players
        for marble in range(1, last_marble + 1):
            if marble % 23 == 0:
                marbles.rotate(-7)

                high_score[marble % players] += marble + marbles.pop()
            else:
                marbles.rotate(2)
                marbles.append(marble)
        return max(high_score)
    return 0


def make_game_larger(game, ratio):
    game_inputs = re.search("([0-9]+) players; last marble is worth ([0-9]+) points", game)
    if game_inputs:
        players = game_inputs.group(1)
        last_marble = int(game_inputs.group(2))

        return players + " players; last marble is worth " + str(last_marble * ratio) + " points"

    return ""


def test1():
    print("Test 1: ")

    with open("inputs/input09.txt", "r") as f:
        game = f.read()[:-1]
    print(get_high_score(game))


def test2():
    print ("Test 2: ")

    with open("inputs/input09.txt", "r") as f:
        game = f.read()[:-1]
    print(get_high_score(make_game_larger(game, 100)))


if __name__ == "__main__":
    test1()
    test2()