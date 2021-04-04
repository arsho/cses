"""
Title     : Missing Number
Category  : Introductory Problems
URL       : https://cses.fi/problemset/task/1083
Author    : arsho
Created   : 04 April 2021
"""


def get_missing_number_solution(n, elements):
    ar = list(map(int, elements.split()))
    return (n * (n + 1)) // 2 - sum(ar)


if __name__ == "__main__":
    total_number = int(input())
    data = input()
    print(get_missing_number_solution(total_number, data))
