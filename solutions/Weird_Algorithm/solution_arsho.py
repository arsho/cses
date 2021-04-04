"""
Title     : Weird Algorithm
Category  : Introductory Problems
URL       : https://cses.fi/problemset/task/1068
Author    : arsho
Created   : 04 April 2021
"""


def get_weird_algorithm_solution(n):
    results = []
    while n != 1:
        results.append(str(n))
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    results.append("1")
    return " ".join(results)


if __name__ == "__main__":
    n = int(input())
    print(get_weird_algorithm_solution(n))
