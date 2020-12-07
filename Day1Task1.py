# Advent of code 2020
# Day 1
# KLPurves

# Example dataframe (from description)

import pandas as pd

dtest = {'Expenses':[1720,979,366,299,1721,1456]}

exp_df = pd.DataFrame(data=dtest)

# task: find the two numbers that add up to 2020. Multiply them.

"""Function that 1. takes the number in the first row and adds it to each qubsequent number one by one 2) checks if the total of this is 2020 (or user specifed amount)
3) if none work, function takes the number in the second row and repeats. 4)when it finds a combination that equals 2020, it stops and multiplies them, returning the output"""


# function to compare starting value to a list and print the answer if the correct combination is found
def add_compare(x,ylist,match):

    for i in ylist:
        compare = int(i[0])
        tot = x+compare
        if tot == match:
            retval = print(str(x) + "+" + str(compare) + "=" + str(x*compare))
            return(retval)
            break
        else:
            continue



# function to start with each index value one by one, comparing to the remainder

def find_expenses(df,amount):
    n_lines = len(df) # get the number of entries to parse

    #loop through the indexes adding each other one and checking if it adds to user specified amount
    for starting in range(n_lines):
        startval = int(df.iloc[starting])
        other_vals = df.iloc[starting+1:n_lines].values.tolist()

        final = add_compare(startval,other_vals,amount)
    return(final)

# run function, idetnfiy the two numbers and the answer
find_expenses(exp_df,2020)
