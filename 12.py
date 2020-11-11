# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Mine Name" starts with "P".
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

new_row = df[df['Mine_Name'].str[0] == 'P']

print(new_row)

