# Advent of code 2020
# Day 2
# KLPurves

# PART ONE
# Validate passwords against a set of rules

import pandas as pd
import re

ex_arr = ['1-3 a: abcde', '1-3 b: cdefg',
          '2-9 c: ccccccccc']

# strategy: Create a function to parse the string
# and gather the rule components into a set of
# variables and the password into another.
# use rule variables to test the password

# define count variable to keep track of number of valid passwords

passcount = 0

def parse_password(stringin):

    global passcount # make count variable global

    for pass in stringin:

        #get first number (lower limit) (ID digit before -)
        lowend = int(re.search(r'(?<!-)\d+', stringin).group())
        # get a number after a - (upper limit)
        upend = int(re.search(r'(?<=-)\d+', stringin).group())
        # get the necessary letter ( 1 0r 0 letter, a-z, looking back from :)
        reqlet = re.search(r'(?<!:)[a-z]', stringin).group()

        # get password characters, strip whitespace, make it a list
        password =  list(re.search(r'(?<=:)\D+', stringin).group().lstrip())

        # get count of required letter in password
        reqcount = password.count(reqlet)

        if reqcount >= lowend & reqcount <= upend:
            passcount += 1
            print(passcount)
        else:
            continue
