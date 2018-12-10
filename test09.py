import unittest
from day09 import get_high_score, make_game_larger


class TestMarbleGame(unittest.TestCase):
    def test_rubbish_input(self):
        self.assertEqual(0, get_high_score(""))

    def test_shortest_game(self):
        self.assertEqual(0, get_high_score("1 players; last marble is worth 0 points"))

    def test_shortest_scoring_game(self):
        self.assertEqual(32, get_high_score("1 players; last marble is worth 23 points"))

    def test_longer_scoring_game(self):
        self.assertEqual(95, get_high_score("1 players; last marble is worth 46 points"))

    def test_longer_scoring_game_two_players(self):
        self.assertEqual(63, get_high_score("2 players; last marble is worth 46 points"))

    def test_first_worked_example(self):
        self.assertEqual(8317, get_high_score("10 players; last marble is worth 1618 points"))

    def test_second_worked_example(self):
        self.assertEqual(146373, get_high_score("13 players; last marble is worth 7999 points"))

    def test_third_worked_example(self):
        self.assertEqual(2764, get_high_score("17 players; last marble is worth 1104 points"))

    def test_forth_worked_example(self):
        self.assertEqual(54718, get_high_score("21 players; last marble is worth 6111 points"))

    def test_fifth_worked_example(self):
        self.assertEqual(37305, get_high_score("30 players; last marble is worth 5807 points"))

    def test_make_game_larger(self):
        self.assertEqual("30 players; last marble is worth 580700 points",
                         make_game_larger("30 players; last marble is worth 5807 points", 100))

    def test_make_another_game_larger(self):
        self.assertEqual("17 players; last marble is worth 11040 points",
                         make_game_larger("17 players; last marble is worth 1104 points", 10))

    def test_make_garbage_game_larger(self):
        self.assertEqual("", make_game_larger("", 10))

    def test_make_game_larger_by_not_mulitple_of_ten(self):
        self.assertEqual("13 players; last marble is worth 42 points",
                         make_game_larger("13 players; last marble is worth 6 points", 7))


if __name__ == "__main__":
    unittest.main()