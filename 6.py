# Write a Pandas program to import excel data (coalpublic2013.xlsx ) skipping first twenty rows into a Pandas dataframe.

def skiprows(n):
    res = []
    for i in range(1,n+1):
        res.append(i)

    return res 

import pandas as pd 
skip = skiprows(20)
df = pd.read_excel('coalpublic2013.xlsx',skiprows=skip)

#print(df)
# Get rows were 'Mine_Name' is 'Calera'
# select = df.loc[df['Mine_Name'] == 'Calera']
# print(select)

# Insert a Row
new_row = {'Year':2020, 'MSHA ID':82317, 'Mine_Name':'Testing', 'Production':9777, 'Labor_Hours':99999}
df = df.append(new_row, ignore_index=True)
print(df)