import math

point_1 = ({"GPSNorthing": 56319, "GPSEasting": 228996})
point_2 = ({"GPSNorthing": 52705, "GPSEasting": 227604})

# Calculate the difference in GPSNorthing and GPSEasting
northing_diff = point_1["GPSNorthing"] - point_2["GPSNorthing"]
easting_diff = point_1["GPSEasting"] - point_2["GPSEasting"]

# Calculate the distance using the Pythagorean theorem
distance = math.sqrt(northing_diff**2 + easting_diff**2)

print(distance/1000)