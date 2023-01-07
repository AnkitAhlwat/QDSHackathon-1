import pandas as pd

df = pd.read_json('file.json')
column = df['column_name']

sum = column.unique().sum()

print(sum)
