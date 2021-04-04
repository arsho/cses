"""
Title     : Distinct Numbers
Category  : Sorting and Searching
URL       : https://cses.fi/problemset/task/1621
Author    : arsho
Created   : 04 April 2021
"""


def get_distinct_values_length(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    mapper = {}
    for i in data:
        mapper[i] = True
    return len(mapper.keys())


if __name__ == "__main__":
    total_values = input()
    values = input()
    print(get_distinct_values_length(total_values, values))
