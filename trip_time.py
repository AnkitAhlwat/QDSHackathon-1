import json
import pandas as pd


trip_data = {}


with open(f'data/data_group0.json', "r") as file_object:
    data = json.load(file_object)

df = pd.DataFrame(data)


df = df.sort_values(by=['SHOVEL_ID', 'DUMP_ID', 'TRUCK_ID', 'TIMESTAMP'])


for (shovel_id, dump_id), group in df.groupby(["SHOVEL_ID", "DUMP_ID"]):
    prev_status = None
    for index, row in group.iterrows():
        if prev_status == 'Hauling' and row['STATUS'] == 'Dumping':
            # Calculate the trip time
            trip_time = row['TIMESTAMP'] - prev_timestamp

            if (shovel_id, dump_id) in trip_data:
                trip_data[(shovel_id, dump_id)]['trip_time'] += trip_time
                trip_data[(shovel_id, dump_id)]['num_trips'] += 1
            else:
                trip_data[(shovel_id, dump_id)] = {'trip_time': trip_time, 'num_trips': 1}
        prev_status = row['STATUS']
        prev_timestamp = row['TIMESTAMP']


avg_trip_time_data = {}
for (shovel_id, dump_id), data in trip_data.items():
    avg_trip_time = data['trip_time'] / data['num_trips']
    avg_trip_time_data[(shovel_id, dump_id)] = round(avg_trip_time / 1000, 2)

# Convert the avg_trip_time_data dictionary to a Pandas DataFrame
avg_trip_time_df = pd.DataFrame.from_dict(avg_trip_time_data, orient='index', columns=['avg_trip_time'])

# Write the avg_trip_time_df DataFrame to a CSV file
avg_trip_time_df.to_csv('data/truck_id_avg_trip_time_data.csv', index=True)

print(avg_trip_time_df)

