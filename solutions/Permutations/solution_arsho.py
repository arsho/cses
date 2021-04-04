"""
Title     : Permutations
Category  : Introductory Problems
URL       : https://cses.fi/problemset/task/1070
Author    : arsho
Created   : 04 April 2021
"""


def get_beautiful_permutation(n):
    if 1 < n < 4:
        return "NO SOLUTION"
    beautiful_permutation = []
    for i in range(2, n + 1, 2):
        beautiful_permutation.append(str(i))
    for i in range(1, n + 1, 2):
        beautiful_permutation.append(str(i))
    return " ".join(beautiful_permutation)


if __name__ == "__main__":
    max_number = int(input())
    print(get_beautiful_permutation(max_number))
