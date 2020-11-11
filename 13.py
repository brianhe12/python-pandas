# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find all records that include two specific MSHA ID.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

id_1 = 102976
id_2 = 103380

# SOLN 1
# options = [id_1,id_2]
# res = df[df['MSHA ID'].isin(options)]

# SOLN 2
res = df[(df['MSHA ID']==id_1) | (df['MSHA ID']==id_2)]
print(res)