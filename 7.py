# Write a Pandas program to add summation to a row of the given excel file.
# https://www.w3resource.com/python-exercises/pandas/excel/index.php#excel
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

production_sum = df['Production'].sum()
labor_sum = df['Labor_Hours'].sum()

df.loc['Total'] = pd.Series([production_sum,labor_sum],index=['Production','Labor_Hours'])

print(df)