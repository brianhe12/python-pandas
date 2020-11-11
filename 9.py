# Write a Pandas program to create a subtotal of "Labor Hours" against MSHA ID from the given excel data (coalpublic2013.xlsx ).
# https://stackoverflow.com/questions/28236305/how-do-i-sum-values-in-a-column-that-match-a-given-condition-using-pandas
import pandas as pd 
df = pd.read_excel('coalpublic2013.xlsx')

# SOLN 1
# Create dataframe
result_df = pd.DataFrame(columns=['MSHA ID','Labor_Hours'])

# Set to check for duplicates
s = set()

# Grab MSHA_ID from Excel
id_col = df['MSHA ID']
for id in id_col:
    if id not in s:
        s.add(id)
        # Sum Labor_Hours where MSHA ID is equal to our current ID that we iterate
        id_sum = df.loc[df['MSHA ID']==id,'Labor_Hours'].sum()
        result_df = result_df.append(pd.Series({"MSHA ID": id,'Labor_Hours':id_sum}), ignore_index=True)

# SOLN 2 - One Liner
# result_df = df.groupby('MSHA ID')['Labor_Hours'].sum()

print(result_df)

