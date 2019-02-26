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


# import numpy as np
from pandas import *
from FighterClass import Fighter
import csv


STATIC_CHOOSE = 3  # rule of limiting the amount of picks within the given options
STATIC_VALUE_UNDER_TEST = 1000000  # rule of limiting the salary

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
    # print(fighter1.get_all_fighter_data())

    # Column order matters
    mma_dk_column_formatting = ['Name + ID', 'Position', 'Name', 'ID', 'Roster Position', 'Salary',
                                'Game Info', 'TeamAbbrev', 'AvgPointsPerGame']

    mma_dk_index_column_formatting = ['Name + ID']
    # with open('draft_kings_mma_(2.23.2019).csv', mode='r') as csv_file:
    # column names are the ones listed above, these have to be in order with the columns of the csv file
    df = pandas.read_csv("draft_kings_mma_(2.23.2019).csv", names=mma_dk_column_formatting, skiprows=0) #, index_col=mma_dk_index_column_formatting
    mma_dk_column_formatting = df.loc[0]
    # df_test = df.set_index("Position")
    num_fighters = 27
    # initializes fighter_list to be in a list of num_fighter elements
    fighter_list = [0]*num_fighters # for i in range(num_fighters)]

    for i in range(1, num_fighters):
        fighter_list[i] = Fighter(1)

        fighter_list[i].name_and_id_number = df[mma_dk_column_formatting[0]][i]
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
        # fighter_list[i].draft_kings_initialization(salary=df[mma_dk_column_formatting[5]][i])

    # position =, name_and_id_number, name, id_number, roster_position, salary,
    # game_info, team_abbrev, avg_point_per_game)

    # fighter1.full_initialization(434, first_name="punch", last_name="fad")

    # print(df['Name + ID', 'TeamAbbrev'])
    # print(df[['Position', 'Name', 'ID', 'Roster Position', 'Salary', 'Game Info', 'TeamAbbrev', 'AvgPointsPerGame']])
    print("11111111111111111111111111")



    # Gets all of game info for all keys
    # print(df[['Game Info']])
    # print(df)

    # print(df_test)
    print("endtestttt~~~~~~~~~~~~~~~~~~~~~~")

    a = [fighter_list[1].salary, fighter_list[2].salary]
    b = [fighter_list[3].salary, fighter_list[4].salary]
    c = [fighter_list[5].salary, fighter_list[6].salary]
    d = [fighter_list[7].salary, fighter_list[8].salary]
    e = []
    f = []
    g = []
    h = []
    j = []
    k = []

    for i in range(1, num_fighters):
        print(fighter_list[i].salary)

    # global variable needed for finding combinations
    count = 0

    find_combinations([a, b, c, e, d, f, g, h, j, k], STATIC_VALUE_UNDER_TEST)

    # n2sBen expand on the idea of combinations that can be any number and
    # also make the method away from main---this is a powerful combinatorial tool
    # print(final_list)

    for i in final_list:
        if i != 0:
            print(i)

    # for i in range(len(final_list)):
    #     if (i % 5) == 0:
    #         print()
    #     if final_list[i] != 0:
    #         print(final_list[i], end = '')
