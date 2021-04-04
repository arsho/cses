"""
Title     : Increasing Array
Category  : Introductory Problems
URL       : https://cses.fi/problemset/task/1094
Author    : arsho
Created   : 04 April 2021
"""


def get_minimum_number_of_moves(n, data):
    n = int(n)
    data = list(map(int, data.split()))
    total_moves = 0
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            diff = data[i - 1] - data[i]
            total_moves += diff
            data[i] += diff
    return total_moves


if __name__ == "__main__":
    total_values = input()
    ar = input()
    print(get_minimum_number_of_moves(total_values, ar))
