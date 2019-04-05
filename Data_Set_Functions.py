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

global data_set_analyzed_sum_salary
global data_set_analyzed_sum_points_per_game
global data_set_analyzed_prediction
# global data_set_analyzed_data_weight

data_set_analyzed_sum_salary = []
data_set_analyzed_sum_points_per_game = []
data_set_analyzed_prediction = []


def data_set_compiled_analyzed_data(input_data):
    global data_set_analyzed_sum_salary
    global data_set_analyzed_sum_points_per_game
    global data_set_analyzed_prediction

    new_3d_list = [None]*len(input_data)

    for i in range(len(input_data)):
        new_3d_list[i] = [input_data[i], data_set_analyzed_sum_salary[i], data_set_analyzed_sum_points_per_game[i]]
        # print(new_3d_list[i][0])

    return new_3d_list


def data_set_filter_by_sum(input_data, sum_required):  # Used primarily for 50k DK salaries

    output_list_num_rows = np.shape(input_data)[0]
    output_list_num_cols = np.shape(input_data)[1]

    output_data = [None] * (len(input_data))

    for i in range(output_list_num_rows):
        one_list_sum_salary = 0
        one_list_analyzed_sum_points_per_game = 0

        for j in range(output_list_num_cols):
            one_list_sum_salary += input_data[i][j].salary
            one_list_analyzed_sum_points_per_game += input_data[i][j].avg_points_per_game

        if one_list_sum_salary <= sum_required:
            output_data[i] = input_data[i]
            data_set_analyzed_sum_salary.append(one_list_sum_salary)
            data_set_analyzed_sum_points_per_game.append(one_list_analyzed_sum_points_per_game)

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


# Sorts data_set by salary or avg_points_per_game

def data_set_sort_by(input_data, attribute, direction):
    if attribute == 'salary' and direction == 'ascending':
        output_data = sorted(input_data, key=lambda x: x[2], reverse=True)
    return output_data#list(filter(None.__ne__, output_data))

