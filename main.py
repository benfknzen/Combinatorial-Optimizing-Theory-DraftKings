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
import csv


STATIC_CHOOSE = 6  # rule of limiting the amount of picks within the given options
STATIC_VALUE_UNDER_TEST = 500000  # rule of limiting the salary

final_list = [None]*30000
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
            n = numbers[i][j] ##Left off 2.26 How do we make sure we do not lose the object class?
            remaining = numbers[i+1:]
            find_mma_fighter_combos(remaining, num_choose, partial + [n])


if __name__ == "__main__":

    # put elements into the same list if the choices restrict the counter choices
    # print(fighter1.get_all_fighter_data())

    # Column order matters
    mma_dk_column_formatting = ['Name + ID', 'Position', 'Name', 'ID', 'Roster Position', 'Salary',
                                'Game Info', 'TeamAbbrev', 'AvgPointsPerGame']

    mma_dk_index_column_formatting = ['Name + ID']
    # with open('draft_kings_mma_(2.23.2019).csv', mode='r') as csv_file:
    # column names are the ones listed above, these have to be in order with the columns of the csv file
    df = pandas.read_csv("draft_kings_mma_(3.2.2019).csv", names=mma_dk_column_formatting, skiprows=0) #, index_col=mma_dk_index_column_formatting
    mma_dk_column_formatting = df.loc[0]
    # df_test = df.set_index("Position")
    num_fighters = 25   # true number of fighters+1
    # initializes fighter_list to be in a list of num_fighter elements
    fighter_list = [0]*num_fighters  # for i in range(num_fighters)]

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

        print(str(fighter_list[i].get_all_draft_kings_data()))
        print()

    print("end reader and player initialization~~~~~~~~~~~~~~~~~~~~~~-------------------------------------------------")

    # a = [fighter_list[1]]
    # b = [fighter_list[3]]
    # c = [fighter_list[12], fighter_list[13]]
    # d = [fighter_list[4]]
    # e = [fighter_list[6]]
    # f = [fighter_list[10], fighter_list[15]]
    # g = [fighter_list[9], fighter_list[16]]
    # h = [fighter_list[5]]
    # i = [fighter_list[11]]
    # j = [fighter_list[7], fighter_list[18]]
    a = [fighter_list[1]]
    b = [fighter_list[5]]
    c = [fighter_list[7], fighter_list[18]]
    d = [fighter_list[4]]
    e = [fighter_list[6]]
    f = [fighter_list[8]]
    g = [fighter_list[9], fighter_list[16]]
    h = [fighter_list[10]]
    i = [fighter_list[11], fighter_list[14]]
    j = [fighter_list[12], fighter_list[13]]

    # global variable needed for finding combinations
    count = 0

    # fighter_list[10].salary = 3000
    # fighter_list[24].salary = 99999 #set for debugging purposes

    find_mma_fighter_combos([a, b, c, d, e, f, g, h, i], STATIC_CHOOSE)

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

    print('There are a total of ' + str(final_list_num_rows) + ' total row combos lineups with a draft of ' + str(final_list_num_cols)
          + ' players per lineup')

    # Filters the data set by sum
    superfinalarray = [None]*final_list_num_rows
    for i in range(final_list_num_rows):
        sum1 = 0
        for j in range(final_list_num_cols):  # final_list[i]:
            # print(final_list[i][j].name_and_id_number + ', ', end='')
            # print(str(final_list[i][j].salary) + ', ', end='')
            sum1 += final_list[i][j].salary
            # print(final_list[i][j].draft_kings_mma_attributes[0] + ', ', end='')
        if sum1 <= 50000:
            superfinalarray[i] = final_list[i]
        # print(str(sum1))


    # Displays the array after filtering
    superfinalarray = list(filter(None.__ne__, superfinalarray))

    a = np.shape(superfinalarray)[0]
    b = np.shape(superfinalarray)[1]
    for i in range(a):
        sum1 = 0
        for j in range(b):  # final_list[i]:
            sum1 += superfinalarray[i][j].salary
            print(superfinalarray[i][j].name_and_id_number + ', ', end='')
        print(str(sum1))

    # print('There are a total of ' + str(final_list_num_rows) + ' unique lineups based on your filter settings')
    print('There are a total of ' + str(np.shape(superfinalarray)[0]) + ' unique lineups based on your filter settings')


#
# add rules and fitness test and rules within the fitness test FPTS points are the most important
# figure out a prediction model based on this
#
# ways to filter an list python