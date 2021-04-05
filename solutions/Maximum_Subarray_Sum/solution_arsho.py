"""
Title     : Maximum Subarray Sum
Category  : Sorting and Searching
URL       : https://cses.fi/problemset/task/1643
Author    : arsho
Created   : 05 April 2021
"""


def get_maximum_subarray_sum_brute_force(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    max_total = 0
    if len(data) > 0:
        max_total = data[0]
        for i in range(len(data) - 1):
            current_total = data[i]
            for j in range(i + 1, len(data)):
                current_total += data[j]
                max_total = max(max_total, current_total)
    return max_total


def get_maximum_subarray_sum(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    max_total = 0
    if len(data) > 0:
        max_total = data[0]
        current_max = data[0]
        for i in range(1, len(data)):
            current_max = max(current_max + data[i], data[i])
            max_total = max(max_total, current_max)
    return max_total


if __name__ == "__main__":
    total_number_of_values = input()
    values = input()
    print(get_maximum_subarray_sum(total_number_of_values, values))
