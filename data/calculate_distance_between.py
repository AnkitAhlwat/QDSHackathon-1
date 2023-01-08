import csv
import math
import pandas as pd

# Set the names of the columns in the CSV files
SHOVEL_ID_COLUMN = 'SHOVEL_ID'
DUMP_ID_COLUMN = 'DUMP_ID'
GPSNORTHING_COLUMN = 'GPSNORTHING'
GPSEASTING_COLUMN = 'GPSEASTING'


# Initialize variables to store the GPS coordinates for each ID
shovel_id_coords = {}
dump_id_coords = {}
distance = {}


# Open the shovel ID CSV file and read the data
with open('shovel_id_location_df.csv', 'r') as file_object:
    reader = csv.DictReader(file_object)
    for row in reader:
        # Get the GPS coordinates for the shovel ID
        shovel_id = row[SHOVEL_ID_COLUMN]
        shovel_northing = float(row[GPSNORTHING_COLUMN])
        shovel_easting = float(row[GPSEASTING_COLUMN])
        shovel_id_coords[shovel_id] = (shovel_northing, shovel_easting)

# Open the dump ID CSV file and read the data
with open('dump_id_location_data.csv', 'r') as file_object:
    reader = csv.DictReader(file_object)
    for row in reader:
        # Get the GPS coordinates for the dump ID
        dump_id = row[DUMP_ID_COLUMN]
        dump_northing = float(row[GPSNORTHING_COLUMN])
        dump_easting = float(row[GPSEASTING_COLUMN])
        dump_id_coords[dump_id] = (dump_northing, dump_easting)

# Iterate over all shovel IDs and dump IDs
for shovel_id, shovel_coords in shovel_id_coords.items():
    for dump_id, dump_coords in dump_id_coords.items():
        # Calculate the distance between the shovel ID and dump ID coordinates using the Pythagorean theorem
        distance_units = math.sqrt((shovel_coords[0] - dump_coords[0])**2 + (shovel_coords[1] - dump_coords[1])**2)
        # Print the result
        distance[f'From {shovel_id} to {dump_id}'] = round(distance_units/1000, 2)


# Convert the location_data dictionary to a Pandas DataFrame
distance_df = pd.DataFrame.from_dict(distance, orient='index')

# Write the location_df DataFrame to a CSV file
distance_df.to_csv('distance.csv', index=True)
print(distance_df)
