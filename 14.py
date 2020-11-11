# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a Pandas dataframe and find a list of specified customers by name.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

def find(options,df):
    return df[df['Mine_Name'].isin(options)]

options = ['Oak Grove Mine','Shoal Creek Mine']
res = find(options,df)
print(res)