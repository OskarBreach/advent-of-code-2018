import unittest
from day07 import build_steps, time_to_complete


class TestInstructionDecoding(unittest.TestCase):
    def setUp(self):
        self.steps = ["Step C must be finished before step A can begin.",
                      "Step C must be finished before step F can begin.",
                      "Step A must be finished before step B can begin.",
                      "Step A must be finished before step D can begin.",
                      "Step B must be finished before step E can begin.",
                      "Step D must be finished before step E can begin.",
                      "Step F must be finished before step E can begin."]

    def tearDown(self):
        self.steps = None

    def test_single_instruction(self):
        self.assertEqual(build_steps([self.steps[0]]), "CA")

    def test_double_instructions(self):
        self.assertEqual(build_steps(self.steps[0:2]), "CAF")

    def test_distinct_instructions(self):
        self.assertEqual(build_steps(self.steps[3:5]), "ABDE")

    def test_all_instructions(self):
        self.assertEqual(build_steps(self.steps), "CABDFE")

    def test_time_to_complete_single_step_single_worker(self):
        self.assertEqual(time_to_complete([self.steps[0]], 1, 0), 4)

    def test_time_to_complete_single_step_single_worker_increased_increments(self):
        self.assertEqual(time_to_complete([self.steps[0]], 1, 60), 124)

    def test_time_to_complete_single_step_double_worker_increased_increments(self):
        self.assertEqual(time_to_complete([self.steps[0]], 2, 60), 124)

    def test_time_to_complete_double_step_single_worker(self):
        self.assertEqual(time_to_complete(self.steps[0:2], 1, 0), 10)

    def test_time_to_complete_double_step_single_worker_increased_increments(self):
        self.assertEqual(time_to_complete(self.steps[0:2], 1, 60), 190)

    def test_time_to_complete_double_step_double_worker_increased_increments(self):
        self.assertEqual(time_to_complete(self.steps[0:2], 2, 60), 129)

    def test_time_taken_for_all_double_workers(self):
        self.assertEqual(time_to_complete(self.steps, 2, 0), 15)


if __name__ == "__main__":
    unittest.main()
