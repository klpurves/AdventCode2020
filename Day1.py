# Advent of code 2020
# Day 1
# KLPurves

# PART ONE
# task: find the two numbers that add up to 2020. Multiply them.
import pandas as pd
import os

# example from site to develop simplest version of function
dtest = {'Expenses': [1721, 979, 366, 299, 675, 1456]}
exp_df = pd.DataFrame(data=dtest)

"""Function that 1. takes the number in the first row and adds it to each
subsequent number one by one 2) checks if the total of this is 2020 (or user
specifed amount)3) if none work, function takes the number in the second row
and repeats. 4)when it finds a combination that equals 2020, it stops and
multiplies them, returning the output"""


# function to compare starting value to a list and print the answer if the
# correct combination is found

def add_compare(x, ylist, match):

    for i in ylist:
        compare = int(i[0])
        tot = x+compare
        if tot == match:
            retval = print(str(x) + "+" + str(compare) + "=" + str(x*compare))
            return(retval)
            break
        else:
            continue

# function to start with each index value one by one,
# comparing to the remainder


def find_expenses(df, amount):
    n_lines = len(df)   # get the number of entries to parse

    # loop through the indexes adding each other one and
    # checking if it adds to user specified amount
    for starting in range(n_lines):
        startval = int(df.iloc[starting])
        other_vals = df.iloc[starting+1:n_lines].values.tolist()

        final = add_compare(startval, other_vals, amount)
    return(final)


# run function, idetnfiy the two numbers and the answer
find_expenses(exp_df, 2020)

# do this with real input.
workdir = os.getcwd()
input = pd.read_csv("{0}/day1task1input.csv".format(workdir), header=None)

find_expenses(input, 2020)

# PART TWO
# task: find the three numbers that add up to 2020. Multiply them.

# Function to add two numbers and each of a remaining list
# and check if these add up to user assigned amount


def add_compare3(x, y, list, match):

    for i in list:
        compare = int(i[0])
        tot = x+y+compare
        if tot == match:
            retval = print(str(x) + "+" + str(y) + "+"
            + str(compare) + "=" + str(x*y*compare))
            return(retval)
            break
        else:
            continue


# Function to compare first two entires to remaining list and
# check if it adds to 2020
# I think the logic here needs to be 1 + 2 + 3, 1 + 2 + 4, 1 + 2 + 5
# then move on to 1 + 3 + 4, 1 + 3 + 5 etc.

def find_expenses3(df, amount):
    n_lines = len(df)   # get the number of entries to parse

    # loop through the indexes adding each other one and
    # checking if it adds to user specified amount
    for starting in range(n_lines):
        for second in range(n_lines-1):
            startval = int(df.iloc[starting])
            secondval = int(df.iloc[second + 1])
            other_vals = df.iloc[second+2:n_lines].values.tolist()

            final = add_compare3(startval, secondval, other_vals, amount)

    return(final)

find_expenses3(exp_df,2020)
