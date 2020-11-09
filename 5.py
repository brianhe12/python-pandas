# Write a Pandas program to insert a column in the sixth position of the said excel sheet and fill it with NaN values.
import pandas as pd 
df = pd.read_excel(r"C:\Users\david he\Desktop\analytics\coalpublic2013.xlsx")

df.insert(5,'Insert Col','NaN')

print(df.head(10))

#df.to_excel('output.xlsx')