# Write a Pandas program to find the sum, mean, max, min value of 'Production (short tons)' column of coalpublic2013.xlsx file.

import pandas as pd 

cols = [3,4]
df = pd.read_excel('coalpublic2013.xlsx')

sum = (df.sum())
print(sum)
output = (df.describe())
print(output)

#output.to_excel('output.xlsx')