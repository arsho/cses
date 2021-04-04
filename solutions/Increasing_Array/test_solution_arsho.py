import unittest

from solutions.Increasing_Array.solution_arsho import \
    get_minimum_number_of_moves


class Test(unittest.TestCase):
    def test_get_minimum_number_of_moves_non_increasing(self):
        n = "10"
        ar = "1000000000 1 1 1 1 1 1 1 1 1"
        result = get_minimum_number_of_moves(n, ar)
        expected_result = 8999999991
        self.assertEqual(result, expected_result,
                         "Error in {}, {}".format(n, ar))

    def test_get_minimum_number_of_moves_mix(self):
        n = "10"
        ar = "6 10 4 10 2 8 9 2 7 7"
        result = get_minimum_number_of_moves(n, ar)
        expected_result = 31
        self.assertEqual(result, expected_result,
                         "Error in {}, {}".format(n, ar))


    def test_get_minimum_number_of_moves_sample(self):
        n = "5"
        ar = "3 2 5 1 7"
        result = get_minimum_number_of_moves(n, ar)
        expected_result = 5
        self.assertEqual(result, expected_result,
                         "Error in {}, {}".format(n, ar))


if __name__ == "__main__":
    unittest.main()