# Write a Pandas program to add summation to a row of the given excel file.
# https://www.w3resource.com/python-exercises/pandas/excel/index.php#excel
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

print(df)
# production_sum = df.sum(level='Production')

# print(production_sum)