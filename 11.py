# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Labor Hours" > 20000.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

rows_greater_than_2000 = df[df['Labor_Hours'] > 20000]

print(rows_greater_than_2000)