import unittest

from solutions.Repetitions.solution_arsho import get_longest_substring_length


class Test(unittest.TestCase):
    def test_get_longest_substring_length(self):
        data = "ATTCGGGA"
        expected_result = 3
        result = get_longest_substring_length(data)
        self.assertEqual(result, expected_result,
                         "Failed in {}\n".format(data))
