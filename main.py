# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng
#
# Execution
#
# Implements all the code and returns a list with combination of lineups
#
# Call csv_append.py in order to append fighter_data.csv with draftkings_mma_(date).csv
# Filter data set with filter_data_set.py in optimal ways
# Use fighter_data.csv to write back into draftkings_mma_(date).csv


#import numpy as np
from pandas import *
from FighterClass import Fighter
import Data_Set_Functions
import datetime

STATIC_CHOOSE = 6  # rule of limiting the amount of picks within the given options
STATIC_VALUE_UNDER_TEST = 50000  # rule of limiting the salary
num_fighters = 20  #true number of fighters+1 also errors if there are no combinations given the number of fighters
STATIC_NUM_LINE_UPS = 20    # creates an error if it is greater than the available num lineups
FILE_NAME = "draft_kings_mma_(8.10.2019).csv" # filename

final_list = [None]*2000000
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

    start = datetime.datetime.now()

    # Column order matters
    mma_dk_column_formatting = ['Name + ID', 'Position', 'Name', 'ID', 'Roster Position', 'Salary',
                                'Game Info', 'TeamAbbrev', 'AvgPointsPerGame', 'Smart Prediction']

    mma_dk_index_column_formatting = ['Name + ID']

    # column names are the ones listed above, these have to be in order with the columns of the csv file
    df = pandas.read_csv("draftking CSV/" + FILE_NAME, names=mma_dk_column_formatting, skiprows=0) #, index_col=mma_dk_index_column_formatting
    mma_dk_column_formatting = df.loc[0]

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

    print("end reader and player initialization~~~~~~~~~~~~~~~~~~~~~~-------------------------------------------------")

    testarray = []
    for i in range(1, num_fighters):
        testarray.append([fighter_list[i]])

    count = 0

    find_mma_fighter_combos(testarray, STATIC_CHOOSE)

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

    final_display_array = Data_Set_Functions.data_set_filter_by_sum(final_display_array, STATIC_VALUE_UNDER_TEST)

    print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after the sum filter')

    # Displays the array after filtering, before the final filter
    #
    # a = np.shape(final_display_array)[0]
    # b = np.shape(final_display_array)[1]
    # for i in range(a):
    #     sum1 = 0
    #     for j in range(b):  # final_list[i]:
    #         sum1 += final_display_array[i][j].salary
    #         print(final_display_array[i][j].name_and_id_number + ', ', end='')
    #     print(str(sum1))

    # print(Data_Set_Functions.data_set_analyzed_sum_salary) #we need it this way so we can sort by weights later


    # prints a brand new 3d array that will be analyzed

    new_3D_data_set = Data_Set_Functions.data_set_compiled_analyzed_data(final_display_array)

    print('#--------------------------------------------------------------------------------------------------------')

    # sorts by total sum of line up avg_points_per_game

    # New 3D being, Raw Lineup Data, Salary Sum, Avg_points_per_game (modified in the csv)

    new_3D_data_set = Data_Set_Functions.data_set_sort_by(new_3D_data_set, 'salary', 'ascending') #was not able to sort via Sum it reduces the list

    # print(new_3D_data_set)
    print('# print data set after sorting-------------------------')
    print(np.shape(new_3D_data_set))
    if STATIC_NUM_LINE_UPS > np.shape(new_3D_data_set)[0]:
        STATIC_NUM_LINE_UPS = np.shape(new_3D_data_set)[0]
    for i in range(STATIC_NUM_LINE_UPS):
        # print(new_3D_data_set[i])
        for j in range(len(new_3D_data_set[i][0])):
                print(new_3D_data_set[i][0][j].name_and_id_number + ', ', end=' ')
        print(str(new_3D_data_set[i][1]) + ', ', end=' ')
        print(new_3D_data_set[i][2])
    print(str(STATIC_NUM_LINE_UPS) + ' line ups are displayed')
    print('There are a total of ' + str(np.shape(final_display_array)[0]) + ' unique lineups after your filter settings')

    finish = datetime.datetime.now()
    print("Execution time:" + str(finish - start))


# add rules and fitness test and rules within the fitness test FPTS points are the most important
# figure out a prediction model based on this
