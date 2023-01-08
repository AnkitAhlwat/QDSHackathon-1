import pandas as pd
import json
import random


with open(f'data/data_group{random.randint(0,9)}.json', "r") as file:
    data = json.load(file)


df = pd.DataFrame.from_dict(data)

hauling_rows = df[df["STATUS"] == "Hauling"]
random_rows = hauling_rows.sample(10)

random_df = pd.DataFrame(random_rows)
random_df.to_csv("random_rows.csv", index=False)


