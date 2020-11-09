# Write a Pandas program to get the data types of the given excel data (coalpublic2013.xlsx ) fields.
import pandas as pd 
df = pd.read_excel(r"C:\Users\david he\Desktop\analytics\coalpublic2013.xlsx")

print(df.dtypes)