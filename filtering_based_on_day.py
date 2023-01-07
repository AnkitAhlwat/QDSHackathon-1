import pandas as pd

df = pd.read_json('BCIT Share/data_group8.json')

df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

df['day'] = df['TIMESTAMP'].dt.day

day = 10
filtered_df = df[df['day'] == day]
print(filtered_df)