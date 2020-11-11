# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find a specific MSHA ID.
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

# Create dataframe
result_df = pd.DataFrame(columns=['MSHA ID','Labor_Hours'])

d = {"MSHA ID": 1,'Labor_Hours':2}
d2 = {"MSHA ID": 231,'Labor_Hours':2123}

dataframe = pd.Series(d)

print(dataframe)
#print(result_df)