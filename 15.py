# Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and find a list of employees where hire_date> 01-01-07.
import pandas as pd 
df = pd.read_excel('employee.xlsx')

res = df[df['hire_date'] > '01-01-07']
print(res)