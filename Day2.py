# Advent of code 2020
# Day 2
# KLPurves

# PART ONE
# Validate passwords against a set of rules

import pandas as pd
import re
import os

# site example
ex_arr = ['1-3 a: abcde', '1-3 b: bdfg',
          '2-9 c: ccccccccd']

# real input
workdir = os.getcwd()
input = pd.read_csv("{0}/day2input.csv".format(workdir), header=None)

input_arr = input[0].tolist()

# strategy: Create a function to parse the string
# and gather the rule components into a set of
# variables and the password into another.
# use rule variables to test the password
# keep a count of valid passwords

# define count variable to keep track of number of valid passwords

passcount = 0


def parse_password(stringin):

    global passcount  # make count variable global

    for item in stringin:

        # get first number (lower limit) (ID digit before -)
        lowend = int(re.search(r'(?<!-)\d+', item).group())
        # get a number after a - (upper limit)
        upend = int(re.search(r'(?<=-)\d+', item).group())
        # get the necessary letter ( 1 0r 0 letter, a-z, looking back from :)
        reqlet = re.search(r'(?<!:)[a-z]', item).group()

        # get password characters, strip whitespace, make it a list
        password = list(re.search(r'(?<=:)\D+', item).group().lstrip())

        # get count of required letter in password
        reqcount = password.count(reqlet)

        if reqcount >= lowend and reqcount <= upend:
            passcount += 1
        else:
            continue
    return(passcount)


# apply to real data

parse_password(input_arr)


# PART TWO
# more complex rule set
# strategy: return required letter indexes isntead of count

# add one to avoid zero indexing issue Function

def reindex(i):
    return(i+1)


sledcount = 0


def sled_password(stringin):

    global sledcount  # make count variable global

    for item in stringin:

        # get first number (lower limit) (ID digit before -)
        lowend = int(re.search(r'(?<!-)\d+', item).group())
        # get a number after a - (upper limit)
        upend = int(re.search(r'(?<=-)\d+', item).group())
        # get the necessary letter ( 1 0r 0 letter, a-z, looking back from :)
        reqlet = re.search(r'(?<!:)[a-z]', item).group()

        # get password characters, strip whitespace, make it a list
        password = re.search(r'(?<=:)\D+', item).group().lstrip()

        # get indexes of reqauired letter matches
        index = [i for i, letter in enumerate(password)
                 if re.search(reqlet, letter)]

        index = list(map(reindex, index))  # fix zero indexing

        if len(index) > 1:
            continue
        elif lowend in index or upend in index:
            sledcount += 1
        else:
            continue

    return(sledcount)


sled_password(ex_arr)
