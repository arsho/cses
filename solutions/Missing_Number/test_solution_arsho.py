from unittest import TestCase

from solutions.Missing_Number.solution_arsho import get_missing_number_solution


class Test(TestCase):
    def test_get_missing_number_solution(self):
        n = 5
        data = "2 3 1 5"
        result = get_missing_number_solution(n, data)
        expected_result = 4
        assert result == expected_result, "Failed in {},\n{}" \
                                          ", Found {}, " \
                                          "Expected {}".format(n, data,
                                                               result,
                                                               expected_result)
