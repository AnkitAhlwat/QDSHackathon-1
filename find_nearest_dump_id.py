import csv
import math
import pandas as pd


DUMP_ID = 'DUMP_ID'
GPSNORTHING = 'GPSNORTHING'
GPSEASTING = 'GPSEASTING'

# Staring Coords
starting_coordinates = [(57326.6, 225337.3), (47.7, -122.4), (47.8, -122.5)]

dump_id_coords = {}
distances = {}

# Dump ID data
with open('data/dump_id_location_data.csv', 'r') as file_object:
    reader = csv.DictReader(file_object)
    for row in reader:
        dump_id = row[DUMP_ID]
        dump_northing_coordinates = float(row[GPSNORTHING])
        dump_easting_coordiantes = float(row[GPSEASTING])
        dump_id_coords[dump_id] = (dump_northing_coordinates, dump_easting_coordiantes)


for current_northing, current_easting in starting_coordinates:
    current_coords = (current_northing, current_easting)

    current_distances = {}
    # Go through all dump_id
    for dump_id, dump_coords in dump_id_coords.items():

        # Calculate the distance  using the Pythagorean theorem
        distance_units = math.sqrt((current_northing - dump_coords[0])**2 + (current_easting - dump_coords[1])**2)
        current_distances[dump_id] = distance_units

    sorted_current_distances = {key: value for key, value in sorted(current_distances.items(), key=lambda item: item[1])}
    nearest_dump_id = list(sorted_current_distances.keys())[0]


    distances[(current_northing, current_easting)] = (nearest_dump_id, sorted_current_distances[nearest_dump_id])

# Results
print('Nearest dump IDs:')
for starting_coords, (dump_id, distance) in distances.items():
    print(f'From starting coordinates {starting_coords}, '
          f'the nearest dump ID is {dump_id}, it is {round(distance/1000,2)} km away ')
