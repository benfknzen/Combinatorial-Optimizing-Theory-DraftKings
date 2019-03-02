# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng, Jordan Shih
#
# Function
#
# Manipulates data specific to our application. A more complex Pandas library.
# Our data consists of arrays within arrays **3-1-2019 BZ Edit
#
# Within this function there will be a Smart_filter which is a weighted approach towards finding optimal solutions while
# taking n-dimensional data. A neural network approach would be worth pursuing.
#
# *From Probability based elimination: When filtering on probability based elimination it is important to focus
# gathering and using data relative to the rules of the game.  Then creating a strong data organizer and
# optimizer based off of this
# raw data, rather than secondary or n-th order data.

import numpy as np
from numpy import exp, array, random, dot
#from pandas import * #conflicts with numpy array for some reason, only import what you need from pandas

global data_set_analyzed_sum
global data_set_analyzed_prediction
# global data_set_analyzed_data_weight

data_set_analyzed_sum = []
data_set_analyzed_prediction = []


def data_set_compiled_analyzed_data(input_data):
    global data_set_analyzed_sum
    global data_set_analyzed_prediction
    new_3d_list = [None]*len(input_data)

    for i in range(len(input_data)):
        new_3d_list[i] = [[input_data[i], data_set_analyzed_sum[i]]]

    return new_3d_list


def data_set_filter_by_sum(input_data, sum_required):  # Used primarily for 50k DK salaries

    output_list_num_rows = np.shape(input_data)[0]
    output_list_num_cols = np.shape(input_data)[1]

    output_data = [None] * (len(input_data))

    for i in range(output_list_num_rows):
        one_list_sum = 0
        for j in range(output_list_num_cols):
            one_list_sum += input_data[i][j].salary
        if one_list_sum <= sum_required:
            output_data[i] = input_data[i]
            data_set_analyzed_sum.append(one_list_sum)

    return list(filter(None.__ne__, output_data))


# Used if one player doing well, usually means the other player is not doing well IE MMA

def data_set_filter_remove_same_game(input_data):
    output_list_num_rows = np.shape(input_data)[0]
    output_list_num_cols = np.shape(input_data)[1]

    output_data = [None] * len(input_data)

    for i in range(output_list_num_rows):
        unique_list = []
        # one_list_attribute = [None] * output_list_num_cols
        # flag_duplicate = 0
        for j in range(output_list_num_cols):
            if input_data[i][j].game_info not in unique_list:
                unique_list.append(input_data[i][j].game_info)
        if len(unique_list) == output_list_num_cols:
            output_data.append(input_data[i])
        # print(unique_list)

    return list(filter(None.__ne__, output_data))


def data_set_sort_by(input_data, attribute, direction):
    # if attribute == 'salary' and direction == 'descending':
    #     print('cool beans')
    # print(input_data)
    output_data = sorted(input_data[0], key=get_key)
    # print("sort data set by attribute and direction")

    return output_data#list(filter(None.__ne__, output_data))


def get_key(item):
    return item[1]

def data_set_remove_player(input_data, fighter_object):
    print("remove lineup by attribute and direction ")


# if __name__ == "__main__":
#
#     # Filtering a list ideas to add ---> *traverse through the array and find out what can fit and what cannot into a final array
#     # In this example we will be taking in 2d lists of object-Fighter
#     # 1. Sum of the line up's salaries needs to be equal to or under 50,000
#     # 1. Line ups that have fighters that have the same fight need to be disposed of
#     # 2. Naming certain fighters should be able to eliminate them from the list
#     # 3.
#     # 4.
#     # 5.
#     # data_set = array([array([1, 2, 3, 5]), array([5, 6])])
#
#     data_set = array([[187, 187, 66, 27, 183, 178, 66, 28], [173, 165, 57, 28, 165, 165, 57, 30],
#                                   [165, 165, 57, 30, 165, 163, 57, 34], [173, 165, 57, 28, 180, 178, 57, 29],
#                                   [165, 165, 57, 30, 168, 163, 57, 26], [185, 185, 71, 35, 188, 188, 71, 27]])
#
#     # data_set *= data_set
#     print(filter_data_set_by_sum(data_set, 850))
#     # for i in data_set:
#     #     print(i)
#     # print((data_set[3]))
