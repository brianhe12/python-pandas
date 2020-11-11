# Write a Pandas program to read specific columns from a given excel file.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

# EX: Read only Column C and Column D
# https://stackoverflow.com/questions/22394598/select-specific-csv-columns-filtering-python-pandas

# Using iloc, could select specific rows/cols
iloc = df.iloc[[0,2,3,4],[1,4]]

# Could also index into dataframe with column names
index = df[['Mine_Name','Production']]

print(iloc.head(10))