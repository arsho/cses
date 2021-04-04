"""
Title     : Apartments
Category  : Sorting and Searching
URL       : https://cses.fi/problemset/task/1084
Author    : arsho
Created   : 05 April 2021
"""


def get_total_distributed_apartments(line_1, line_2, line_3):
    n, m, k = list(map(int, line_1.split()))
    desired_sizes = sorted(list(map(int, line_2.split())))
    apartment_sizes = sorted(list(map(int, line_3.split())))
    distributed_apartment = 0
    for desired_size in desired_sizes:
        for i, v in enumerate(apartment_sizes):
            if v - k <= desired_size <= v + k:
                del apartment_sizes[i]
                distributed_apartment += 1
                break
            if v - k > desired_size:
                break
    return distributed_apartment


if __name__ == '__main__':
    data_1 = input()
    data_2 = input()
    data_3 = input()
    print(get_total_distributed_apartments(data_1, data_2, data_3))
