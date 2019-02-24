# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng, Jordan Shih
#
# Execution
#
# Implements all the code and returns a list with combination of lineups
#
# Call csv_append.py in order to append fighter_data.csv with draftkings_mma_(date).csv
# Filter dataset with filter_data_set.py in optimal ways
# Use fighter_data.csv to write back into draftkings_mma_(date).csv


# import numpy as np
from pandas import *

STATIC_CHOOSE = 3 #rule of limiting the amount of picks within the given options
STATIC_VALUE_UNDER_TEST = 50 # rule of limiting the salary

final_list = [0]*30000
global count


def find_combinations(numbers, target, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s <= target and len(partial) == STATIC_CHOOSE:  # required length
        global count
        final_list[count] = partial
        count = count + 1
    else:
         final_list.remove(0)

    if s > target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            n = numbers[i][j]
            remaining = numbers[i+1:]
            find_combinations(remaining, target, partial + [n])


if __name__ == "__main__":

    # put elements into the same list if the choices restrict the counter choices

    a = [1, 2, 3, 4]
    b = [5, 6, 7]
    c = [8, 9]
    d = []
    e = []
    f = []
    g = []
    h = []
    j = []
    k = []

    count = 0

    find_combinations([a, b, c, e, d, f, g, h, j, k], STATIC_VALUE_UNDER_TEST)

    # print(final_list)

    for i in final_list:
        if i != 0:
            print(i)

    # for i in range(len(final_list)):
    #     if (i % 5) == 0:
    #         print()
    #     if final_list[i] != 0:
    #         print(final_list[i], end = '')
