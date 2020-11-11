# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find a specific MSHA ID.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

def find(id,df):
    return df[df['MSHA ID']==id]


print(find(102901,df))