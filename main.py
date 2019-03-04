# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng, Jordan Shih
#
# Execution
#
# Implements all the code and returns a list with combination of lineups
#
# Call csv_append.py in order to append fighter_data.csv with draftkings_mma_(date).csv
# Filter data set with filter_data_set.py in optimal ways
# Use fighter_data.csv to write back into draftkings_mma_(date).csv


import numpy as np
from pandas import *
from FighterClass import Fighter
import Data_Set_Functions


STATIC_CHOOSE = 6  # rule of limiting the amount of picks within the given options
STATIC_VALUE_UNDER_TEST = 500000  # rule of limiting the salary

final_list = [None]*200000
global count
# global sumtest


# def find_combinations(numbers, target, partial=[]):
#     s = sum(partial)
#     # check if the partial sum is equals to target
#
#     if s <= target and len(partial) == STATIC_CHOOSE:  # required length
#         global count
#         final_list[count] = partial
#         count = count + 1
#     else:
#         final_list.remove(0)
#
#     if s > target:
#         return  # if we reach the number why bother to continue
#
#     for i in range(len(numbers)):
#         for j in range(len(numbers[i])):
#             n = numbers[i][j]
#             remaining = numbers[i+1:]
#             find_combinations(remaining, target, partial + [n])


def find_mma_fighter_combos(numbers, num_choose,  partial=[]):
    # sum_fighter_salary = sum(Fighter.salary for Fighter in partial)

    if len(partial) == num_choose:  # required length
        global count
        final_list[count] = partial
        count = count + 1

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            n = numbers[i][j]
            remaining = numbers[i+1:]
            find_mma_fighter_combos(remaining, num_choose, partial + [n])


if __name__ == "__main__":

    # put elements into the same list if the choices restrict the counter choices
    # print(fighter1.get_all_fighter_data())

    # Column order matters
    mma_dk_column_formatting = ['Name + ID', 'Position', 'Name', 'ID', 'Roster Position', 'Salary',
                                'Game Info', 'TeamAbbrev', 'AvgPointsPerGame']

    mma_dk_index_column_formatting = ['Name + ID']
    # with open('draft_kings_mma_('date').csv', mode='r') as csv_file:
    # column names are the ones listed above, these have to be in order with the columns of the csv file
    df = pandas.read_csv("draft_kings_mma_(3.2.2019).csv", names=mma_dk_column_formatting, skiprows=0) #, index_col=mma_dk_index_column_formatting
    mma_dk_column_formatting = df.loc[0]
    num_fighters = 25   # true number of fighters+1

    # initializes fighter_list to be in a list of num_fighter elements
    fighter_list = [0]*num_fighters

    for i in range(1, num_fighters):
        fighter_list[i] = Fighter(1)

        fighter_list[i].name_and_id_number = df[mma_dk_column_formatting[0]][i]
        fighter_list[i].draft_kings_mma_attributes[0] = df[mma_dk_column_formatting[1]][i] #test
        fighter_list[i].position = df[mma_dk_column_formatting[1]][i]
        fighter_list[i].name = df[mma_dk_column_formatting[2]][i]
        fighter_list[i].id_number = int(df[mma_dk_column_formatting[3]][i])
        fighter_list[i].roster_position = df[mma_dk_column_formatting[4]][i]
        fighter_list[i].salary = float(df[mma_dk_column_formatting[5]][i])
        fighter_list[i].game_info = df[mma_dk_column_formatting[6]][i]
        fighter_list[i].team_abbrev = df[mma_dk_column_formatting[7]][i]
        fighter_list[i].avg_points_per_game = float(df[mma_dk_column_formatting[8]][i])

        # prints out the fighter data
        # print(str(fighter_list[i].get_all_draft_kings_data()))
        # print()

    print("end reader and player initialization~~~~~~~~~~~~~~~~~~~~~~-------------------------------------------------")

    # a = array([fighter_list[1]])
    # b = array([fighter_list[2]])
    # c = array([fighter_list[3]])
    # d = array([fighter_list[4]])
    # e = array([fighter_list[5]])
    # f = array([fighter_list[6]])
    # g = array([fighter_list[7]])
    # h = array([fighter_list[8]])
    # i = array([fighter_list[9]])
    # j = array([fighter_list[10]])
    # k = array([fighter_list[11]])
    # loo = array([fighter_list[12]])
    # looi = array([fighter_list[13]])
    # m = array([fighter_list[14]])
    # n = array([fighter_list[15]])
    # o = array([fighter_list[16]])
    # p = array([fighter_list[17]])
    # q = array([fighter_list[18]])
    # r = array([fighter_list[19]])
    # s = array([fighter_list[20]])
    # t = array([fighter_list[21]])
    # u = array([fighter_list[22]])
    # v = array([fighter_list[23]])
    # w = array([fighter_list[24]])
    #
    # # global variable needed for finding combinations
    # count = 0
    #
    # # fighter_list[10].salary = 3000
    # # fighter_list[24].salary = 99999 #set for debugging purposes
    #
    # find_mma_fighter_combos([a, b, c, d, e, f, g, h, i, j, k, loo, looi, m, n, o,  p, q, r, s, t, u, v, w], STATIC_CHOOSE)

    # Simplified input to reduce processing time

    a = array([fighter_list[1]])
    b = array([fighter_list[2]])
    c = array([fighter_list[3]])
    d = array([fighter_list[4]])
    e = array([fighter_list[5]])
    f = array([fighter_list[6]])
    g = array([fighter_list[7]])
    h = array([fighter_list[8]])
    i = array([fighter_list[9]])
    j = array([fighter_list[10]])
    k = array([fighter_list[11]])
    loo = array([fighter_list[12]])
    looi = array([fighter_list[13]])
    m = array([fighter_list[14]])
    n = array([fighter_list[15]])
    o = array([fighter_list[16]])



    count = 0

    # fighter_list[10].salary = 3000
    # fighter_list[24].salary = 99999 #set for debugging purposes

    find_mma_fighter_combos([a, b, c, d, e, f, g, h, i, j, k, loo, looi, m, n, o], STATIC_CHOOSE)

    #-------------------------------------------------------------
    # Filter data set I should be able to add all the fighters in the list--- IE
    # find_mma_fighter_combos([Fight Card], STATIC_CHOOSE)
    # Then just add a rule of eliminating same fight card fighters from the set---traverse through and delete yourself
    # if you have the same game info as another
    #-------------------------------------------------------------

    # Filters the final list to remove blanks
    final_list = list(filter(None.__ne__, final_list))

    # Prints the total rows
    final_list_num_rows = np.shape(final_list)[0]
    final_list_num_cols = np.shape(final_list)[1]
    if final_list_num_rows != 0:
        print('There are a total of ' + str(final_list_num_rows) + ' total row combos lineups with a draft of ' + str(final_list_num_cols)
          + ' players per lineup')
    else:
        print('There are no line ups possible given your input')

    # data_set_filter_remove_same_game

    final_display_array = Data_Set_Functions.data_set_filter_remove_same_game(final_list)

    print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after the unique game filter')

    # Filters the data set by sum

    final_display_array = Data_Set_Functions.data_set_filter_by_sum(final_display_array, 50000)

    print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after the sum filter')


    # Before we sort we must first make sure to finish off the 3D matrix otherwise we will not get to analyze it well**

    # final_display_array =
    # Data_Set_Functions.data_set_sort_by(final_display_array, 'salary', 'descending')
    #
    # print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after the sort filter')

    # final_display_array = Data_Set_Functions.data_set_remove_player(final_display_array, )
    #
    # print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after the no player filter')

    print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after same game filter')
    # Displays the array after filtering

    a = np.shape(final_display_array)[0]
    b = np.shape(final_display_array)[1]
    for i in range(a):
        sum1 = 0
        for j in range(b):  # final_list[i]:
            sum1 += final_display_array[i][j].salary
            print(final_display_array[i][j].name_and_id_number + ', ', end='')
        print(str(sum1))
    print('-----------------------------------------------------------------------------------------------------------')
    print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups based on your filter settings')
    print('There are a total of ' + str(np.shape(final_display_array)) + ' unique parameters based on your filter settings')
    print('-----------------------------------------------------------------------------------------------------------')

    print(Data_Set_Functions.data_set_analyzed_sum) #we need it this way so we can sort by weights later

    print('# prints a brand new 3d array that will be analyzed')
    # prints a brand new 3d array that will be analyzed

    new_3D_data_set = Data_Set_Functions.data_set_compiled_analyzed_data(final_display_array)
    print(new_3D_data_set[13][0][1])

    # in order to traverse into our new array we must go to print(new_3D_data_set[1][0][0][0].salary) 'lol wow'
    # a = np.shape(new_3D_data_set)[0]
    # b = np.shape(new_3D_data_set)[1]
    # for i in range(a):
    #     sum1 = 0
    #     for j in range(b):  # final_list[i]:
    #         sum1 += final_display_array[i][j].salary
    #         print(final_display_array[i][j].name_and_id_number + ', ', end='')
    #     print(str(sum1))

    print('#--------------------------------------------------------------------------------------------------------')

    # a = np.shape(new_3D_data_set)[0]
    # b = np.shape(new_3D_data_set)[1]
    # print(str(a) + ' by ' + str(b))
    print(np.shape(new_3D_data_set))

    # sorts by

    new_3D_data_set = Data_Set_Functions.data_set_sort_by(new_3D_data_set, 'salary', 'descending') #was not able to sort via Sum it reduces the list

    # print(new_3D_data_set)
    print('# print data set after sorting-------------------------')
    print(np.shape(new_3D_data_set))
    for i in range(np.shape(final_display_array)[0]):
        for j in range(6):
                print(new_3D_data_set[i][0][j].name_and_id_number + ', ', end= ' ')
        print()



# add rules and fitness test and rules within the fitness test FPTS points are the most important
# figure out a prediction model based on this
