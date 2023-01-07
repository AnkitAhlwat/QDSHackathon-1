import json
import pandas as pd

# Initialize the dictionary
location_data = {}

for dump_id in range(36):
    location_data[dump_id] = {
        "TIMESTAMP": 0,
    }

# Loop through each file
for file_number in range(10):
    # Read the JSON file
    with open(f'data/data_group{file_number}.json', "r") as file_object:
        data = json.load(file_object)

    # Convert the JSON data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Select rows with STATUS equal to Dumping
    df = df[df['STATUS'] == 'Dumping']

    # Group the DataFrame by DUMP_ID
    grouped_df = df.groupby("DUMP_ID")

    # For each dump ID and status combination, find the row with the maximum TIMESTAMP
    for dump_id, group in grouped_df:
        # Find the row with the maximum TIMESTAMP for this group
        max_row = group.loc[group['TIMESTAMP'].idxmax()]
        # Store the GPSNORTHING and GPSEASTING values for this group
        if max_row["TIMESTAMP"] > location_data[dump_id]["TIMESTAMP"]:
            location_data[dump_id] = max_row

# Convert the location_data dictionary to a Pandas DataFrame
location_df = pd.DataFrame.from_dict(location_data, orient='index')

# Write the location_df DataFrame to a CSV file
location_df.to_csv('data/dump_id_location_data.csv', index=False)


print(location_df)