"""
Title     : Repetitions
Category  : Introductory Problems
URL       : https://cses.fi/problemset/task/1069
Author    : arsho
Created   : 04 April 2021
"""


def get_longest_substring_length(s):
    max_length = 0
    current_length = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    max_length = max(max_length, current_length)
    return max_length


if __name__ == "__main__":
    s = input()
    print(get_longest_substring_length(s))