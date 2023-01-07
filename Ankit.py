import json
import pandas as pd

with open(f'data/data_group0.json', "r") as f:
    # Load the JSON data
    data = json.load(f)

df = pd.DataFrame(data)
grouped_df = df.groupby("SHOVEL_ID")

# Iterate over the groups
for shovel_id, group in grouped_df:
    group.to_csv(f"shovel_{shovel_id}.csv", index=False)

# Display the data
print(df)