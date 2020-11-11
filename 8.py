# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a Pandas dataframe and display the last ten rows.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

print(df.tail(10))