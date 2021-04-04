import unittest

from solutions.Distinct_Numbers.solution_arsho import \
    get_distinct_values_length


class Test(unittest.TestCase):
    def test_get_distinct_values_length(self):
        total_values = "5"
        values = "2 3 2 2 3"
        expected_result = 2
        result = get_distinct_values_length(total_values, values)
        self.assertEqual(expected_result, result,
                         "Error in {}, {}".format(
                             total_values,
                             values
                         ))
