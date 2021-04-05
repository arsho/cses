import unittest

from solutions.Maximum_Subarray_Sum.solution_arsho import \
    get_maximum_subarray_sum


class Test(unittest.TestCase):
    def test_get_maximum_subarray_sum_sample(self):
        n = "8"
        ar = "-1 3 -2 5 3 -5 2 2"
        expected_result = 9
        result = get_maximum_subarray_sum(n, ar)
        self.assertEqual(result, expected_result,
                         "Failed in {}, {}".format(n, ar))


    def test_get_maximum_subarray_sum_book_sample(self):
        n = "8"
        ar = "-1 2 4 -3 5 2 -5 2"
        expected_result = 10
        result = get_maximum_subarray_sum(n, ar)
        self.assertEqual(result, expected_result,
                         "Failed in {}, {}".format(n, ar))


if __name__ == "__main__":
    unittest.main()