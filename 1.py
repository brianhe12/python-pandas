# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a Pandas dataframe
import pandas as pd 

df = pd.read_excel('coalpublic2013.xlsx')

print(df.head)